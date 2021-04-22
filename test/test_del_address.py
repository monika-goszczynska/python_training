from model.address import Address
from random import randrange


def test_delete_some_address(app):
    if app.address.count() == 0:
        app.address.new(Address(first_name="test", middle_name="test", last_name="test"))
    old_addresses = app.address.get_address_list()
    index = randrange(len(old_addresses))
    app.address.delete_address_by_index(index)
    # assert len(old_addresses) - 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses[index:index+1] = []
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)