# -*- coding: utf-8 -*-
import time

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new(Group(name="1212", header="13131", footer="1414"))
    app.group.return_to_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    time.sleep(1)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new(Group(name="", header="", footer=""))
    app.group.return_to_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    time.sleep(1)
