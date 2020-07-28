from datetime import datetime

from app.plugin import db


class Company(db.Model):
    """合作公司"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(200), unique=False, nullable=False)
    person = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=False)
    c_type = db.Column(db.String(10), nullable=False)
    active = db.Column(db.Boolean, default=True)
    record = db.Column(db.Text)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "person": self.person,
            "address": self.address,
            "phone": self.phone,
            "c_type": self.c_type,
            "record": self.record,
            "create_time": self.create_time
        }
