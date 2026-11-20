import os
import random
import string
import urllib.parse

from flask import Flask, render_template, request, redirect, abort
from werkzeug.middleware.proxy_fix import ProxyFix

from config import Config
from models import db, URL

import qrcode

app = Flask(__name__)

# Handle reverse proxies (e.g., Render, Heroku) so request.host_url correctly resolves to https
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


def is_valid_url(url):
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme in ("http", "https"), result.netloc])
    except Exception:
        return False


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
    qr_path = None
    short_code = None
    error = None

    if request.method == "POST":

        original_url = request.form.get("url", "").strip()

        if original_url:
            if not original_url.startswith(("http://", "https://")):
                original_url = "https://" + original_url

            if not is_valid_url(original_url):
                error = "Please enter a valid URL (e.g. https://example.com)."
            else:
                short_code = generate_short_code()

                new_url = URL(
                    original_url=original_url,
                    short_code=short_code
                )

                db.session.add(new_url)
                db.session.commit()

                short_url = request.host_url + short_code
                
                qr_filename = f"{short_code}.png"
                qr_path = f"qr/{qr_filename}"
                
                img = qrcode.make(short_url)
                
                os.makedirs(
                    "static/qr",
                    exist_ok=True
                )
                
                img.save(
                    f"static/qr/{qr_filename}"
                )

    return render_template(
        "index.html",
        short_url=short_url,
        short_code=short_code,
        qr_path=qr_path,
        error=error
    )

@app.route("/<short_code>")
def redirect_to_original(short_code):
    # Ignore favicon.ico and other browser asset probes
    if short_code in ("favicon.ico", "robots.txt", "static"):
        abort(404)

    url = URL.query.filter_by(short_code=short_code).first()
    if not url:
        return render_template(
            "index.html",
            error="Short URL not found or has expired."
        ), 404
    
    url.clicks += 1
    db.session.commit()

    return redirect(url.original_url)


if __name__ == "__main__":
    app.run(debug=True)