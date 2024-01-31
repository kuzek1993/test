import time

from model.group import Group


def test_add_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.change_description(Group(name="1212", header="13131", footer="1414"))
    app.group.return_to_group()
    app.session.logout()
    time.sleep(1)