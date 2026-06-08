import random
import string

from flask import Flask, render_template, request , redirect

from config import Config
from models import db, URL

import qrcode
import os

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        short_code = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        existing = URL.query.filter_by(
            short_code=short_code
        ).first()

        if not existing:
            return short_code


@app.route("/", methods=["GET", "POST"])
def home():

    short_url = None

    if request.method == "POST":

        original_url = request.form.get("url")

        short_code = generate_short_code()

        new_url = URL(
            original_url=original_url,
            short_code=short_code
        )

        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + short_code
        
        qr_path = f"qr/{short_code}.png"
        
        img = qrcode.make(short_url)
        
        os.makedirs(
            "static/qr",
            exist_ok=True
        )
        
        img.save(
            f"static/qr/{short_code}.png"
        )

    return render_template(
        "index.html",
        short_url=short_url,
        qr_path=qr_path if short_url else None
    )

@app.route("/<short_code>")
def redirect_to_original(short_code):
    url = URL.query.filter_by(short_code=short_code).first()
    if not url:
        return "<h2>URL not found</h2>", 404
    
    url.clicks += 1
    db.session.commit()

    return redirect(url.original_url)

@app.route("/dashboard")
def dashboard():

    search = request.args.get("search", "")

    if search:

        urls = URL.query.filter(
            URL.original_url.contains(search)
        ).all()

    else:

        urls = URL.query.order_by(
            URL.created_at.desc()
        ).all()

    total_urls = URL.query.count()

    total_clicks = sum(
        url.clicks for url in URL.query.all()
    )

    top_urls = (
        URL.query
        .order_by(URL.clicks.desc())
        .limit(5)
        .all()
    )

    chart_labels = [
        url.short_code
        for url in top_urls
    ]

    chart_data = [
        url.clicks
        for url in top_urls
    ]
    
    most_visited = (
        URL.query
        .order_by(URL.clicks.desc())
        .first()
    )

    return render_template(
        "dashboard.html",
        urls=urls,
        search=search,
        total_urls=total_urls,
        total_clicks=total_clicks,
        chart_labels=chart_labels,
        chart_data=chart_data,
        most_visited= most_visited
    )


@app.route("/delete/<int:id>")
def delete_url(id):

    url = URL.query.get_or_404(id)

    db.session.delete(url)

    db.session.commit()

    return redirect("/dashboard")


if __name__ == "__main__":
    app.run(debug=True)