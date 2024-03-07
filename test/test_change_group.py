import time
from model.group import Group
from random import randrange
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_new(Group(name="модификация"))
    old_groups = db.get_group_list()
    new = Group(name="new group", footer="new footer", header="new header")
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, new)
    new_groups = db.get_group_list()
    for i in range(0, len(old_groups)):
        if old_groups[i].id == group.id:
            old_groups[i] = new
    assert len(old_groups) == len(new_groups)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    time.sleep(1)
