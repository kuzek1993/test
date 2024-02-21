# -*- coding: utf-8 -*-
import time
import pytest
import random
import string
from model.contact import Contact

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(first_name=first_name, last_name=last_name,
                    mobilephone=mobilephone)
     for first_name in ["", random_string("first_name", 10)]
     for last_name in ["", random_string("last_name", 10)]
     for mobilephone in ["", random_string("mobilephone", 10)]
     ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
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

