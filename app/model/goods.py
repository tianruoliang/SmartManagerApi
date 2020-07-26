from datetime import datetime

from app.plugin import db

class Goods(db.Model):
    """库存"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    g_type = db.Column(db.String(80), unique=False, nullable=False)
    total = db.Column(db.Integer, nullable=False, default=0)
    goods_in = db.relationship('GoodsIn', backref='goods', lazy='dynamic', cascade='all, delete-orphan')
    goods_out = db.relationship('GoodsOut', backref='goods', lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "g_type": self.g_type,
            "total": self.total
        }


class GoodsIn(db.Model):
    """进库记录"""

    id = db.Column(db.Integer, primary_key=True)
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id', ondelete='CASCADE'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    record = db.Column(db.Text, nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())

    staff = db.relationship("Staff", lazy="joined")
    company = db.relationship("Company", lazy="joined")

    def to_dict(self):
        return {
            "id": self.id,
            "staff": self.staff.name,
            "company": self.company.name,
            "number": self.number,
            "record": self.record,
            "create_time": self.create_time
        }


class GoodsOut(db.Model):
    """出库记录"""

    id = db.Column(db.Integer, primary_key=True)
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id', ondelete='CASCADE'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    record = db.Column(db.Text, nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())

    staff = db.relationship("Staff", lazy="joined")
    company = db.relationship("Company", lazy="joined")

    def to_dict(self):
        return {
            "id": self.id,
            "staff": self.staff.name,
            "company": self.company.name,
            "number": self.number,
            "record": self.record,
            "create_time": self.create_time
        }
