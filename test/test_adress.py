def test_adress_on_homepage(app):
    adress_from_homepage = app.contact.get_contact_list() [0]
    adress_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert adress_from_homepage.adress == (adress_from_editpage.adress)