import time

from model.group import Group


def test_modify_group_name(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.change_description(Group(name="1212", header="13131", footer="1414"))
    app.group.return_to_group()
    app.session.logout()
    time.sleep(1)