# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.click_add(wd)
        self.create_contact(wd, firts_name=u"Иванов", last_name=u"Иван")
        self.return_homepage(wd)
        self.logout(wd)

    def test_add_contact_empty(self):
        wd = self.wd
        self.home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.click_add(wd)
        self.create_contact(wd, firts_name=u"", last_name=u"")
        self.return_homepage(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_homepage(self, wd):
        # return to homepage
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd, firts_name, last_name):
        # add atribute
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firts_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("1212")
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def click_add(self, wd):
        # click add new
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, user_name, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
