from datetime import datetime

from app.model import db


class Company(db.Model):
    """合作公司"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(200), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=False)
    c_type = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "c_type": self.c_type,
            "create_time": self.create_time
        }
