
from pytest_bdd import given, when, then
from model.address import Address


@given("an address list", target_fixture="address_list")
def address_list(db):
    return db.get_address_list()


@given("an address with <first_name>, <middle_name> and <last_name>", target_fixture="new_address")
def new_address(first_name, middle_name, last_name):
    return Address(first_name=first_name, middle_name=middle_name, last_name=last_name)


@when("I add the address to the list")
def add_address(app, new_address):
    app.address.new(new_address)


@then("the new address list is equal to old address list with the added address")
def verify_address_added(db, address_list, new_address):
    old_addresses = address_list
    new_addresses = db.get_address_list()
    old_addresses.append(new_address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)