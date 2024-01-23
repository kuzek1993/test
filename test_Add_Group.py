# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_new_group()
    app.add_description(Group(name="1212", header="13131", footer="1414"))
    app.creation_group()
    app.return_to_group()
    app.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_new_group()
    app.add_description(Group(name="", header="", footer=""))
    app.creation_group()
    app.return_to_group()
    app.logout()
