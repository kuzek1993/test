import time
from model.contact import Contact
from random import randrange
def test_change_contact(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name=u"Удоли", last_name=u"Меня", phone="Скорее"))
    index = randrange(len(old_contact))
    contact = Contact(first_name=u"Иванов", last_name=u"Иван", phone="1212")
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    time.sleep(1)