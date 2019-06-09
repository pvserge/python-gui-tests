from random import randrange


def test_delete_random_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) < 2:
        app.groups.add_new_group("my group")
    group_index = randrange(1, len(old_list))
    app.groups.delete_group_by_index(group_index)
    new_list = app.groups.get_group_list()
    old_list.pop(group_index)
    assert sorted(old_list) == sorted(new_list)
