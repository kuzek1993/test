# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from contact import Contact
class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        self.home_page()
        self.login(user_name="admin", password="secret")
        self.click_add()
        self.create_contact(Contact(first_name=u"Иванов", last_name=u"Иван", phone="1212"))
        self.return_homepage()
        self.logout()

    def test_add_contact_empty(self):
        self.home_page()
        self.login(user_name="admin", password="secret")
        self.click_add()
        self.create_contact(Contact(first_name=u"", last_name=u"", phone=""))
        self.return_homepage()
        self.logout()

    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

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

    def login(self, user_name, password):
        # login
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def home_page(self):
        # open home page
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
