from model.group import Group
from random import randrange


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    old_groups = db.get_group_list()
    random_index = randrange(0, len(old_groups))
    group = old_groups[random_index]
    app.group.modify_group_by_id(group.id, Group(name="NewName", header="NewHeader", footer="NewFooter"))
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[random_index] = new_groups[random_index]
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test", header="test", footer="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test", header="test", footer="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="New footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
