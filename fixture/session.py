class SessionHelper:

    def __init__(self, app):
        self.app = app
    def login(self, username, password):
        wd = self.app.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//*/text()[normalize-space(.)='']/parent::*").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.logget_in():
            self.logout()

    def logget_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text == "("+username+")"


    def logget_in(self):
        wd = self.app.wd
        return len(wd.find_element_by_link_text("Logout")) > 0

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.logget_in():
            if self.logget_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
