
from model.contact import Contact
import time
import re

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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def add_contact_to_group(self, id):
        wd = self.app.wd
        self.home_page()
        self.select_contact_by_id(id)
        time.sleep(1)
        wd.find_element_by_name("add").click()

    def delete_contact_to_group(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        time.sleep(1)
        wd.find_element_by_name("remove").click()






    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]") [index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def change_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']") [index].click()
        self.form_contact(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.home_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s" % id).click()
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
                form = element.find_elements_by_tag_name("td")
                last_name = form[1].text
                first_name = form[2].text
                id = form[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = form[5].text
                all_email = form[4].text
                adress = form[3].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id, all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_email, adress=adress))
        return list(self.contact_cache)
    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']") [index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        adress = wd.find_element_by_name("address").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, email1=email1, email2=email2, email3=email3, adress=adress)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone)


    def get_email_list(self, index):
        wd = self.app.wd
