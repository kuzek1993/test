def test_name_on_homepage(app):
    name_from_homepage = app.contact.get_contact_list() [0]
    name_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert name_from_homepage.first_name == (name_from_editpage.first_name)
    assert name_from_homepage.last_name == (name_from_editpage.last_name)