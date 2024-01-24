# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from appcontact import Appcontact


@pytest.fixture
def app(request):
    fixture = Appcontact()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.home_page()
    app.login(user_name="admin", password="secret")
    app.click_add()
    app.create_contact(Contact(first_name=u"Иванов", last_name=u"Иван", phone="1212"))
    app.return_homepage()
    app.logout()

def test_add_contact_empty(app):
    app.home_page()
    app.login(user_name="admin", password="secret")
    app.click_add()
    app.create_contact(Contact(first_name=u"", last_name=u"", phone=""))
    app.return_homepage()
    app.logout()

