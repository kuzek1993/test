class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_homepage(self):
        # return to homepage
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self):
        # add atribute
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def change_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def click_add(self):
        # click add new
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
    def update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
