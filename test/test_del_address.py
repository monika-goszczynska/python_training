from model.address import Address
import random


def test_delete_some_address(app, db, check_ui):
    if len(db.get_address_list()) == 0:
        app.address.new(Address(first_name="test", middle_name="test", last_name="test"))
    old_addresses = db.get_address_list()
    address = random.choice(old_addresses)
    # index = randrange(len(old_addresses))
    app.address.delete_address_by_id(id)
    new_addresses = db.get_address_list()
    assert len(old_addresses) - 1 == len(new_addresses)
    old_addresses.remove(address)
    assert old_addresses == new_addresses
    if check_ui:
        assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)