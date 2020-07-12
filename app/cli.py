import click
from flask.cli import AppGroup

from app.controller.user import create_user
from app.model.role import Role
from app.plugin import db

db_cli = AppGroup('db', help="Database client", short_help='List database script.')


@db_cli.command("init", short_help="Init all tables.")
def init_db():
    db.drop_all()
    db.create_all()
    Role.init_role()


@db_cli.command("create-admin", short_help="Add admin")
@click.argument('name')
@click.argument('username')
@click.argument('password')
def create_admin(name, username, password):
    admin_role = Role.query.filter_by(name="admin").first()
    create_user({
        "name": name,
        "username": username,
        "password": password,
        "role_id": admin_role.id
    })


def init_cli(app):
    app.cli.add_command(db_cli)
