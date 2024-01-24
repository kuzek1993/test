# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from contact import Contact
from appcontact import Appcontact
class AddContact(unittest.TestCase):
    def setUp(self):
        self.app = Appcontact()
    
    def test_add_contact(self):
        self.app.home_page()
        self.app.login(user_name="admin", password="secret")
        self.app.click_add()
        self.app.create_contact(Contact(first_name=u"Иванов", last_name=u"Иван", phone="1212"))
        self.app.return_homepage()
        self.app.logout()

    def test_add_contact_empty(self):
        self.app.home_page()
        self.app.login(user_name="admin", password="secret")
        self.app.click_add()
        self.app.create_contact(Contact(first_name=u"", last_name=u"", phone=""))
        self.app.return_homepage()
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
