# -*- coding: utf-8 -*-
from model.contact import Contact
import time

    
def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.click_add()
    app.contact.create_contact(Contact(first_name=u"Иванов", last_name=u"Иван", phone="1212"))
    app.contact.return_homepage()
    app.session.logout()
    time.sleep(1)

def test_add_contact_empty(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.click_add()
    app.contact.create_contact(Contact(first_name=u"", last_name=u"", phone=""))
    app.contact.return_homepage()
    app.session.logout()
    time.sleep(1)

