# -*- coding: utf-8 -*-
import time
from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create_new(group)
    app.group.return_to_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    time.sleep(1)


#def test_add_empty_group(app):
    #old_groups = app.group.get_group_list()
    #group = Group(name="", header="", footer="")
    #app.group.create_new(group)
    #app.group.return_to_group()
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) + 1 == len(new_groups)
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    #time.sleep(1)
