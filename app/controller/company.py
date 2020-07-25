from app.model.company import Company
from app.plugin import db


def get_company_list(page_info):
    pagination = Company.query.paginate(**page_info)
    return pagination


def get_company_detail(cid):
    company = Company.query.get_or_404(cid)
    return company


def create_company(info):
    company = Company(**info)
    db.session.add(company)
    db.session.commit()
    return company


def delete_company(cid):
    company = Company.query.get_or_404(cid)
    db.session.delete(company)
    db.session.commit()
    return company


def put_company(cid, info):
    Company.query.filter_by(id=cid).update(info)
    db.session.commit()
    db.session.close()
    return Company.query.get_or_404(cid)
