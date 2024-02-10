import time

from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create_new(Group(name="модификация"))
    app.group.change_description(Group(name="new group"))
    app.group.return_to_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    time.sleep(1)

def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.change_description(Group(header="new header"))
    app.group.return_to_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    time.sleep(1)

def test_modify_group_footer(app):
    old_groups = app.group.get_group_list()
    app.group.change_description(Group(footer="1414"))
    app.group.return_to_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    time.sleep(1)