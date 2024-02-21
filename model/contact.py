from sys import maxsize

class Contact:
    def __init__(self, first_name=None, last_name=None, mobilephone=None, workphone=None, homephone=None, secondaryphone=None, email1=None,
                 email2=None, email3=None, all_phones_from_home_page=None, all_email_from_home_page=None, adress=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.homephone = homephone
        self.secondaryphone = secondaryphone
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page
        self.adress = adress
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.first_name, self.last_name, self.mobilephone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize