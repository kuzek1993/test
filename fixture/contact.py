class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_homepage(self):
        # return to homepage
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact):
        # add atribute
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.form_contact(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()




    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def change_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.form_contact(contact)
        wd.find_element_by_name("update").click()



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
        wd.find_element_by_name("mobile").send_keys(contact.phone)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
