import re
from model.contact import Contact


def test_attribute_on_homepage(app, db):


    attribute_ui_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name, last_name=contact.last_name, mobilephone=contact.mobilephone, email1=contact.email1,
                       email2=contact.email2, email3=contact.email3, adress=contact.adress, homephone=contact.homephone, workphone=contact.workphone)
    attribute_from_db = sorted(map(clean, db.get_contact_list()), key=Contact.id_or_max)
    for i in range(0, len(attribute_ui_from_homepage)):
        assert attribute_ui_from_homepage[i].first_name == attribute_from_db[i].first_name
        assert attribute_ui_from_homepage[i].last_name == attribute_from_db[i].last_name
        assert attribute_ui_from_homepage[i].all_phones_from_home_page == merge_phones_on_homepage(attribute_from_db[i])
        assert attribute_ui_from_homepage[i].all_email_from_home_page == merge_email_on_homepage(attribute_from_db[i])
        assert attribute_ui_from_homepage[i].adress == attribute_from_db[i].adress



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
