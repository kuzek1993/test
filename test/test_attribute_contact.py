import re

def test_attribute_on_homepage(app):
    attribute_from_homepage = app.contact.get_contact_list() [0]
    attribute_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert attribute_from_homepage.all_email_from_home_page == merge_email_on_homepage(attribute_from_editpage)
    assert attribute_from_homepage.all_phones_from_home_page == merge_phones_on_homepage(attribute_from_editpage)
    assert attribute_from_homepage.first_name == (attribute_from_editpage.first_name)
    assert attribute_from_homepage.last_name == (attribute_from_editpage.last_name)
    assert attribute_from_homepage.adress == (attribute_from_editpage.adress)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_email_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), [contact.email1, contact.email2, contact.email3, ])))
def merge_phones_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, ]))))


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == (contact_from_editpage.homephone)
    assert contact_from_view_page.mobilephone == (contact_from_editpage.mobilephone)
    assert contact_from_view_page.workphone == (contact_from_editpage.workphone)
