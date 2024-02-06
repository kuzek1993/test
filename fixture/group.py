


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create_new(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.group_form(group)
        wd.find_element_by_name("submit").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def change_description(self, change_form_value):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.group_form(change_form_value)
        wd.find_element_by_name("update").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def group_form(self, group):
        wd = self.app.wd
        self.change_form_value("group_name", group.name)
        self.change_form_value("group_header", group.header)
        self.change_form_value("group_footer", group.footer)

    def change_form_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
