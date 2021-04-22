from model.address import Address
from random import randrange


def test_modify_first_name(app):
    if app.address.count() == 0:
        app.address.new(Address(first_name="test", middle_name="test", last_name="test"))
    old_addresses = app.address.get_address_list()
    index = randrange(len(old_addresses))
    address = Address(first_name="New first name")
    address.id = old_addresses[index].id
    app.address.modify_address_by_index(index, address)
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) == len(new_addresses)
    old_addresses[index] = address
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)


#def test_modify_bday(app):
#    if app.address.count() == 0:
#        app.address.new(Address(first_name="test", middle_name="test", last_name="test"))
#    old_addresses = app.address.get_address_list()
#    app.address.modify_first_address(Address(birth_day="6"))
#    new_addresses = app.address.get_address_list()
#    assert len(old_addresses) == len(new_addresses)
