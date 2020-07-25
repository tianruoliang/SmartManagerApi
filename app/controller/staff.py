from app.model.staff import Staff
from app.plugin import db


def get_staff_list():
    data = Staff.query.all()
    return [d.to_dict() for d in data]


def create_staff(info):
    staff = Staff(**info)
    db.session.add(staff)
    db.session.commit()
    return staff.to_dict()


def get_staff_detail(sid):
    staff = Staff.query.get_or_404(sid)
    return staff.to_dict()


def delete_staff_detail(sid):
    staff = Staff.query.get_or_404(sid)
    db.session.delete(staff)
    db.session.commit()
    return staff.to_dict()
