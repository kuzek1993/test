import re
from model.contact import Contact


def test_attribute_on_homepage(app, db):


    attribute_ui_from_homepage = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name, last_name=contact.last_name, mobilephone=contact.mobilephone, email1=contact.email1,
                       email2=contact.email2, email3=contact.email3, adress=contact.adress, homephone=contact.homephone, workphone=contact.workphone)
    attribute_from_db = map(clean, db.get_contact_list())
    assert sorted(attribute_ui_from_homepage, key=Contact.id_or_max) == sorted(attribute_from_db, key=Contact.id_or_max)
    #assert attribute_ui_from_homepage.all_phones_from_home_page == attribute_from_db
    #assert attribute_ui_from_homepage.first_name == attribute_from_db
    #assert attribute_ui_from_homepage.last_name == attribute_from_db
    #assert attribute_ui_from_homepage.adress == attribute_from_db

def clear(s):
    return re.sub("[() -]", "", s)

def merge_email_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                            [contact.email1, contact.email2, contact.email3, ])))
def merge_phones_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, ]))))


#def test_phones_on_contact_view_page(app):
    #contact_from_view_page = app.contact.get_contact_from_view_page(0)
    #contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    #assert contact_from_view_page.homephone == (contact_from_editpage.homephone)
    #assert contact_from_view_page.mobilephone == (contact_from_editpage.mobilephone)
    #assert contact_from_view_page.workphone == (contact_from_editpage.workphone)
