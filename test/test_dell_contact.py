import time

def test_delete_contact(app):
    app.contact.delete_first_contact()
    time.sleep(1)