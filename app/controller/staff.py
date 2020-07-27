from app.model.staff import Staff
from app.plugin import db


def get_staff_all():
    return [staff.to_dict() for staff in Staff.query.all()]


def get_staff_list(page_info):
    pagination = Staff.query.paginate(**page_info)
    return pagination


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
    staff.active = False
    db.session.add(staff)
    db.session.commit()
    return staff
