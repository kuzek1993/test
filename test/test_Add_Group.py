# -*- coding: utf-8 -*-
import time

import pytest
import random
import string

from model.group import Group

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
            Group(name=name, header=header, footer=footer)
            for name in ["", random_string("name", 10)]
            for header in ["", random_string("header", 20)]
            for footer in ["", random_string("footer", 20)]
    ]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
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
