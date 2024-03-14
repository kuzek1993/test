from model.contact import Contact
import random
from model.group import Group
from fixture.orm import ORMFixture


orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")



def test_delete_contact_to_group(app, db):
    contact = Contact(first_name=u"Удоли", last_name=u"Меня", mobilephone="Скорее")
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(contact)
    if len(db.get_group_list()) == 0:
        app.group.create_new(Group(name="для удаления"))
    if len(orm.get_contacts_not_in_any_group()) == len(db.get_contact_list()):
        contact = db.get_contact_list()
        select_contact = random.choice(contact)
        group = db.get_group_list()
        select_group = random.choice(group)
        app.group.select_group_by_ui(select_group.id)
        app.contact.add_contact_to_group(select_contact.id)

    group_contact = orm.get_groups_with_contacts()
    select_group = random.choice(group_contact)


    app.group.select_group_by_contact(select_group.id)
    contacts = orm.get_contacts_in_group(select_group)
    select_contact = random.choice(contacts)
    app.contact.delete_contact_to_group(select_contact.id)
    new_contact = orm.get_contacts_in_group(select_group)
    assert len(contacts) - 1 == len(new_contact)
    assert select_contact in contacts and select_contact not in new_contact


