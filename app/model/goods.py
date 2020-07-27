from datetime import datetime

from app.plugin import db

class Goods(db.Model):
    """库存"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    g_type = db.Column(db.String(80), unique=False, nullable=False)
    total = db.Column(db.Integer, nullable=False, default=0)
    cost_price = db.Column(db.Float, nullable=False, default=0)  # 成本总价 默认为 0
    sales_price = db.Column(db.Float, nullable=False, default=0)  # 销售总价 默认为 0
    goods_records = db.relationship(
        'GoodsRecord', backref='goods', lazy='dynamic', cascade='all, delete-orphan'
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "g_type": self.g_type,
            "total": self.total,
            "cost_price": self.cost_price,
            "sales_price": self.sales_price
        }


class GoodsRecord(db.Model):
    """进出库记录"""

    id = db.Column(db.Integer, primary_key=True)
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id', ondelete='CASCADE'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    g_type = db.Column(db.String(10), nullable=False)  # in 进库 out 出库
    single_price = db.Column(db.Float, nullable=False)  # 单价
    number = db.Column(db.Integer, nullable=False)
    record = db.Column(db.Text, nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now())

    staff = db.relationship("Staff", lazy="joined")
    company = db.relationship("Company", lazy="joined")

    def to_dict(self):
        return {
            "id": self.id,
            "goods_name": self.goods.name,
            "goods_g_type": self.goods.g_type,
            "staff": self.staff.name,
            "company": self.company.name,
            "g_type": self.g_type,
            "single_price": self.single_price,
            "number": self.number,
            "record": self.record,
            "create_time": self.create_time
        }
