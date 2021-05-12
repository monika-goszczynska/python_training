from model.address import Address
from random import randrange


def test_modify_first_name(app, db, check_ui):
    if app.address.count() == 0:
        app.address.new(Address(first_name="test", middle_name="test", last_name="test"))
    old_addresses = db.get_address_list()
    id = randrange(0, len(old_addresses))
    address = old_addresses[id]
    app.address.modify_address_by_id(address.id, Address(first_name="Nju", last_name="Nju"))
    new_addresses = db.get_address_list()
    assert len(old_addresses) == len(new_addresses)
    old_addresses[id] = address
    assert old_addresses == new_addresses
    if check_ui:
        assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_address_list(), key=Address.id_or_max)


#def test_modify_bday(app):
#    if app.address.count() == 0:
#        app.address.new(Address(first_name="test", middle_name="test", last_name="test"))
#    old_addresses = app.address.get_address_list()
#    app.address.modify_first_address(Address(birth_day="6"))
#    new_addresses = app.address.get_address_list()
#    assert len(old_addresses) == len(new_addresses)
