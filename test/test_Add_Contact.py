# -*- coding: utf-8 -*-
import time
from model.contact import Contact

def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contact = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    time.sleep(1)

#def test_add_contact_empty(app):
    #old_contact = app.contact.get_contact_list()
    #contact = Contact(first_name=u"", last_name=u"", mobilephone="")
    #app.contact.create_contact(contact)
    #new_contact = app.contact.get_contact_list()
    #assert len(old_contact) + 1 == len(new_contact)
    #old_contact.append(contact)
    #assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    #time.sleep(1)

