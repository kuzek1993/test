import time
from model.contact import Contact
def test_change_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.change_first_contact()
    app.atribute_contact.Atribute(Contact(first_name=u"Иванов", last_name=u"Иван", phone="1212"))
    app.contact.update()
    app.contact.return_homepage()
    app.session.logout()
    time.sleep(1)