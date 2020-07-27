from app.model.goods import Goods
from app.plugin import db


def get_goods_list(page_info):
    pagination = Goods.query.paginate(**page_info)
    return pagination


def get_goods_detail(gid):
    return Goods.query.get_or_404(gid)


def create_goods(info):
    goods = Goods(**info)
    db.session.add(goods)
    db.session.commit()
    return goods.to_dict()


def delete_goods(gid):
    goods = Goods.query.get_or_404(gid)
    db.session.delete(goods)
    db.session.commit()
    return goods.to_dict()
