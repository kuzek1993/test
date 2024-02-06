import time

from model.group import Group


def test_modify_group_name(app):
    app.group.change_description(Group(name="new group"))
    app.group.return_to_group()
    time.sleep(1)

def test_modify_group_header(app):
    app.group.change_description(Group(header="new header"))
    app.group.return_to_group()
    time.sleep(1)

def test_modify_group_footer(app):
    app.group.change_description(Group(footer="1414"))
    app.group.return_to_group()
    time.sleep(1)