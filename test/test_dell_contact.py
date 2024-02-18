import time
from model.contact import Contact
from random import randrange
def test_delete_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(first_name=u"Удоли", last_name=u"Меня", mobilephone="Скорее")
    if app.contact.count() == 0:
        app.contact.create_contact(contact)
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact[index:index+1] = []
    assert old_contact == new_contact
    time.sleep(1)