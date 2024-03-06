import time
from model.contact import Contact
import random
from random import randrange
def test_change_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(first_name=u"Удоли", last_name=u"Меня", mobilephone="Скорее"))
    old_contact = db.get_contact_list()
    index = randrange(len(old_contact))
    new = Contact(first_name=u"Иванов", last_name=u"Иван", mobilephone="1212")
    contact = random.choice(old_contact)
    new.id = contact.id
    app.contact.modify_contact_by_id(contact.id, new)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = new
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=contact.id_or_max)
    time.sleep(1)