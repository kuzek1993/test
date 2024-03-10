from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
   contacts = db.get_not_contacts_in_group(Group(id="300"))
   for contact in contacts:
       print(contact)
   print(len(contacts))
finally:
    pass #db.destroy()