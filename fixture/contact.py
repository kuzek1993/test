
from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def create_contact(self, contact):
        # add atribute
        wd = self.app.wd
        self.home_page()
        wd.find_element_by_link_text("add new").click()
        self.form_contact(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]") [index].click()

    def change_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']") [index].click()
        self.form_contact(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("Delete")) > 0):
            wd.find_element_by_link_text("home").click()

    def form_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                last_name = element.find_element_by_css_selector("td:nth-child(2)").text
                first_name = element.find_element_by_css_selector("td:nth-child(3)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id))
        return list(self.contact_cache)


