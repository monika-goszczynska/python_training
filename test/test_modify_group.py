from model.group import Group
from random import randrange


def test_modify_group_name(app, db, check_ui):
    #jesli pusto tworzymy grupe
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    # zapisujemy grupe przed modyf z bazy danych
    old_groups = db.get_group_list()
    #wybieramy losowy element z grupy przed modyf.
    id = randrange(0, len(old_groups))
    group = old_groups[id]
    # modyfikujemy grupe
    app.group.modify_group_by_id(group.id, Group(name="newname", header="newheader", footer="newfooter"))
    # zapisujemy grupe po modyf z bazy danych
    new_groups = db.get_group_list()
    # porownujemy dlugosc list
    assert len(old_groups) == len(new_groups)
    # zastepujemy stara grupe zmodyfikowana
    old_groups[id] = group
    # poronujemy stara i nowa grupe
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
