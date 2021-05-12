# -*- coding: utf-8 -*-
from model.address import Address


def test_add_address(app, db, check_ui, json_addresses):
    address = json_addresses
    old_addresses = db.get_address_list()
    app.address.new(address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = db.get_address_list()
    old_addresses.append(address)
    assert old_addresses == new_addresses
    if check_ui:
        assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_address_list(), key=Address.id_or_max)
