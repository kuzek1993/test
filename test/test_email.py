import re

def test_email_on_homepage(app):
    email_from_homepage = app.contact.get_contact_list() [0]
    email_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert clear(email_from_homepage.all_email_from_home_page) == merge_email_on_homepage(email_from_editpage)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_email_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), [contact.email1, contact.email2, contact.email3, ])))
