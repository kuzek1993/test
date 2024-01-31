


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def add_description(self, group):
        wd = self.app.wd
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

    def create_new(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        wd = self.app.wd
        # open_groups_page
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()

    def change_description(self, group):
        wd = self.app.wd
        # add_group_description
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("update").click()
