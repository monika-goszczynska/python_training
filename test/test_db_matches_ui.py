from model.group import Group
from model.address import Address
from timeit import timeit


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_address_list(app, db):
    ui_list = app.address.get_address_list()
    def clean(address):
        return Address(id=address.id, first_name=address.first_name.strip(), last_name=address.last_name.strip())
    db_list = map(clean, db.get_address_list())
    assert sorted(ui_list, key=Address.id_or_max) == sorted(db_list, key=Address.id_or_max)