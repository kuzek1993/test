from selenium import webdriver
from fixture.session import SessionHelper
class Appcontact:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def return_homepage(self):
        # return to homepage
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact):
        # add atribute
        wd = self.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.phone)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def click_add(self):
        # click add new
        wd = self.wd
        wd.find_element_by_link_text("add new").click()


    def home_page(self):
        # open home page
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()