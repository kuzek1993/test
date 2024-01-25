# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.app_contact import Appcontact


@pytest.fixture
def app(request):
    fixture = Appcontact()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.home_page()
    app.session.login(username="admin", password="secret")
    app.contact.click_add()
    app.contact.create_contact(Contact(first_name=u"Иванов", last_name=u"Иван", phone="1212"))
    app.contact.return_homepage()
    app.session.logout()

def test_add_contact_empty(app):
    app.home_page()
    app.session.login(username="admin", password="secret")
    app.contact.click_add()
    app.contact.create_contact(Contact(first_name=u"", last_name=u"", phone=""))
    app.contact.return_homepage()
    app.session.logout()

