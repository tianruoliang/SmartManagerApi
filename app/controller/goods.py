from flask import abort

from app.model.goods import Goods, GoodsIn, GoodsOut
from app.plugin import db


def get_goods_list(page_info):
    pagination = Goods.query.paginate(**page_info)
    return pagination


def get_goods_detail(gid):
    return Goods.query.get_or_404(gid)


def get_goods_in_list(gid, page_info):
    goods = Goods.query.get_or_404(gid)
    pagination = goods.goods_in.paginate(**page_info)
    pagination.items = [x.to_dict() for x in pagination.items]
    return pagination


def get_goods_out_list(gid, page_info):
    goods = Goods.query.get_or_404(gid)
    pagination = goods.goods_out.paginate(**page_info)
    pagination.items = [x.to_dict() for x in pagination.items]
    return pagination


def create_goods(info):
    goods = Goods(**info)
    db.session.add(goods)
    db.session.commit()
    return goods.to_dict()


def create_goods_in(gid, info):
    goods = Goods.query.get_or_404(gid)
    goods_in = GoodsIn(goods_id=gid, **info)
    goods.total += info.get('number')
    db.session.add(goods)
    db.session.add(goods_in)
    db.session.commit()
    return goods_in.to_dict()


def create_goods_out(gid, info):
    goods = Goods.query.get_or_404(gid)
    if goods.total >= info.get('number'):
        goods.total -= info.get('number')
    else:
        abort(500, '库存不足')
    goods_out = GoodsOut(goods_id=gid, **info)
    db.session.add(goods)
    db.session.add(goods_out)
    db.session.commit()
    return goods_out.to_dict()


def delete_goods(gid):
    goods = Goods.query.get_or_404(gid)
    db.session.delete(goods)
    db.session.commit()
    return goods.to_dict()
