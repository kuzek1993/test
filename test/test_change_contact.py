import time
from model.contact import Contact
import random
def test_change_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(first_name=u"Удоли", last_name=u"Меня", mobilephone="Скорее"))
    old_contact = db.get_contact_list()

    new = Contact(first_name=u"Иванов", last_name=u"Иван", mobilephone="1212")
    contact = random.choice(old_contact)
    app.contact.modify_contact_by_id(contact.id, new)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    time.sleep(1)