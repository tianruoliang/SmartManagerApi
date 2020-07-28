from flask import abort
from app.model.goods import Goods, GoodsRecord
from app.plugin import db


def get_goods_record_list(page_info, condition):
    pagination = GoodsRecord.query.filter_by(**condition).paginate(**page_info)
    pagination.items = [x.to_dict() for x in pagination.items]
    return pagination


def create_goods_record(info):
    goods = Goods.query.get_or_404(info['goods_id'])
    total = goods.total
    cost_price = goods.cost_price
    sales_price = goods.sales_price
    number = info['number']
    single_price = info['single_price']
    if info['g_type'] == 'in':
        total += number
        cost_price += number * single_price
    else:
        if total >= number:
            total -= number
            sales_price += number * single_price
        else:
            abort(500, '库存不足')
    goods_record = GoodsRecord(**info)
    goods.total = total
    goods.cost_price = cost_price
    goods.sales_price = sales_price
    db.session.add(goods)
    db.session.add(goods_record)
    db.session.commit()
    return goods_record.to_dict()
