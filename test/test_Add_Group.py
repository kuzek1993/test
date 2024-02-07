# -*- coding: utf-8 -*-
import time

from model.group import Group


def test_add_group(app):
    app.group.create_new(Group(name="1212", header="13131", footer="1414"))
    app.group.return_to_group()
    time.sleep(1)


def test_add_empty_group(app):
    app.group.create_new(Group(name="", header="", footer=""))
    app.group.return_to_group()
    time.sleep(1)
