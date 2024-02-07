import time
from model.contact import Contact
def test_change_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name=u"Удоли", last_name=u"Меня", phone="Скорее"))
        app.contact.return_homepage()
    app.contact.change_first_contact(Contact(first_name=u"Иванов", last_name=u"Иван", phone="1212"))
    app.contact.return_homepage()
    time.sleep(1)