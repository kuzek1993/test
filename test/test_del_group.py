
import time
from model.group import Group
from random import randrange
def test_delete_some_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create_new(Group(name="для удаления"))
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    app.group.return_to_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
    time.sleep(1)