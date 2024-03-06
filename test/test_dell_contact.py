import time
from model.contact import Contact
import random
def test_delete_contact(app, db, check_ui):
    contact = Contact(first_name=u"Удоли", last_name=u"Меня", mobilephone="Скорее")
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(contact)
    old_contact = db.get_contact_list()
    select = random.choice(old_contact)
    app.contact.delete_contact_by_id(select.id)
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact.remove(select)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=contact.id_or_max)
    time.sleep(1)