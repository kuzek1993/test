# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.create_new()
    app.group.add_description(Group(name="1212", header="13131", footer="1414"))
    app.group.creation()
    app.group.return_to_group()
    app.session.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.create_new()
    app.group.add_description(Group(name="", header="", footer=""))
    app.group.creation()
    app.group.return_to_group()
    app.session.logout()
