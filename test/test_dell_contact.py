import time
from model.contact import Contact
def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name=u"Удоли", last_name=u"Меня", phone="Скорее"))
        app.contact.return_homepage()
    app.contact.delete_first_contact()
    time.sleep(1)