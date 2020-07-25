from app.model.staff import Staff
from app.plugin import db


def get_staff_list():
    return Staff.query.all()


def create_staff(info):
    staff = Staff(**info)
    db.session.add(staff)
    db.session.commit()
    return staff


def get_staff_detail(sid):
    staff = Staff.query.get_or_404(sid)
    return staff


def delete_staff_detail(sid):
    staff = Staff.query.get_or_404(sid)
    db.session.delete(staff)
    db.session.commit()
    return staff
