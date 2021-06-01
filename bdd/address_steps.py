
from pytest_bdd import given, when, then
from model.address import Address
import random


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


@given("a non-empty address list", target_fixture="non_empty_address_list")
def non_empty_address_list(db, app):
    if len(db.get_address_list()) == 0:
        app.address.new(Address(first_name="FName", middle_name="MName", last_name="LName"))
    return db.get_address_list()


@given("a random address from the list", target_fixture="random_address")
def random_address(non_empty_address_list):
    return random.choice(non_empty_address_list)


@when("I delete the address from the list")
def delete_address(app, random_address):
    app.address.delete_address_by_id(random_address.id)


@then("the new address list is equal to the old address list without the deleted address")
def verify_address_deleted(db, non_empty_address_list, random_address, app, check_ui):
    old_addresses = non_empty_address_list
    new_addresses = db.get_address_list()
    assert len(old_addresses) - 1 == len(new_addresses)
    old_addresses.remove(random_address)
    assert old_addresses == new_addresses
    if check_ui:
        assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_address_list(),
                                                                      key=Address.id_or_max)


@when("I modify the address from the list")
def modify_address(app, random_address):
    app.address.modify_address_by_id(random_address.id, Address(first_name="FNameMod", last_name="LNameMod"))


@then("the new address list is equal to the old address list with the modified address")
def verify_address_modified(app, db, check_ui, non_empty_address_list, random_address):
    old_addresses = non_empty_address_list
    new_addresses = db.get_address_list()
    old_addresses[random_address.id] = random_address

