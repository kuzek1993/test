import pymysql.cursors
from model.group import Group
from model.contact import Contact





class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                [id, name, header, footer] = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))

        finally:
            cursor.close()
        return list
    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id,firstname,lastname,mobile,address,home,work,email,email2,email3 from addressbook")
            for row in cursor:
                [id, firstname, lastname, mobile, address, home, work, email, email2, email3] = row
                list.append(Contact(id=str(id), first_name=firstname, last_name=lastname, mobilephone=mobile, adress=address, homephone=home,
                                    workphone=work, email1=email, email2=email2, email3=email3))

        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

