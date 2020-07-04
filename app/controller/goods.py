from app.model import db
from app.model.goods import Goods, GoodsIn, GoodsOut


def get_goods_list():
    data = Goods.query.all()
    return [d.to_dict() for d in data]


def get_goods_detail(gid):
    goods = Goods.query.get_or_404(gid)
    return goods.to_dict()


def create_goods(info):
    goods = Goods(**info)
    db.session.add(goods)
    db.session.commit()
    return goods.to_dict()


def get_goods_in_list():
    data = GoodsIn.query.all()
    return [d.to_dict() for d in data]


def get_goods_out_list():
    data = GoodsOut.query.all()
    return [d.to_dict() for d in data]
