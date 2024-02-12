import time
from random import randrange
from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create_new(Group(name="модификация"))
    index = randrange(len(old_groups))
    group = Group(name="new group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    time.sleep(1)

#def test_modify_group_header(app):
    #old_groups = app.group.get_group_list()
    #app.group.change_description(Group(header="new header"))
    #app.group.return_to_group()
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
    #time.sleep(1)

#def test_modify_group_footer(app):
    #old_groups = app.group.get_group_list()
    #app.group.change_description(Group(footer="1414"))
    #app.group.return_to_group()
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
    #time.sleep(1)