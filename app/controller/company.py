from app.model import db
from app.model.company import Company


def get_company_list():
    data = Company.query.all()
    return [d.to_dict() for d in data]


def get_company_detail(cid):
    company = Company.query.get_or_404(cid)
    return company.to_dict()


def create_company(info):
    company = Company(**info)
    db.session.add(company)
    db.session.commit()
    return company.to_dict()


def delete_company(cid):
    company = Company.query.get_or_404(cid)
    db.session.delete(company)
    db.session.commit()
    return company.to_dict()
