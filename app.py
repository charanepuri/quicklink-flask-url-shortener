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


if __name__ == "__main__":
    app.run(debug=True)