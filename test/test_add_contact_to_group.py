from model.contact import Contact
import random
from model.group import Group
from fixture.orm import ORMFixture


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")



def test_add_contact_to_group(app, db):
    contact = Contact(first_name=u"Удоли", last_name=u"Меня", mobilephone="Скорее")
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(contact)
    if len(db.get_group_list()) == 0:
        app.group.create_new(Group(name="для удаления"))
    if len(orm.get_contacts_not_in_any_group()) == 0:
        app.contact.create_contact(contact)

    contact = orm.get_contacts_not_in_any_group()
    select_contact = random.choice(contact)
    group = db.get_group_list()
    select_group = random.choice(group)
    old_contact_in_group = orm.get_contacts_in_group(select_group)
    app.group.select_group_by_ui(select_group.id)
    app.contact.add_contact_to_group(select_contact.id)
    new_contact_in_group = orm.get_contacts_in_group(select_group)
    assert select_contact not in old_contact_in_group and select_contact in new_contact_in_group