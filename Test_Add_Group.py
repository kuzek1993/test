# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_new_group()
        self.add_description(Group(name="1212", header="13131", footer="1414"))
        self.creation_group()
        self.return_to_group()
        self.logout()

    def test_add_empty_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_new_group()
        self.add_description(Group(name="", header="", footer=""))
        self.creation_group()
        self.return_to_group()
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_group(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def add_description(self, group):
        wd = self.wd
        # add_group_description
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create_new_group(self):
        wd = self.wd
        wd.find_element_by_name("new").click()

    def creation_group(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        wd = self.wd
        # open_groups_page
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//*/text()[normalize-space(.)='']/parent::*").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()