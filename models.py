from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class URL(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    original_url = db.Column(
        db.String(500),
        nullable=False
    )

    short_code = db.Column(
        db.String(10),
        unique=True,
        nullable=False
    )

    clicks = db.Column(
        db.Integer,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<URL {self.short_code}>"