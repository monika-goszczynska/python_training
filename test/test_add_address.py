# -*- coding: utf-8 -*-
from model.address import Address


def test_add_address(app, db, json_addresses):
    address = json_addresses
    old_addresses = db.get_address_list()
    app.address.new(address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = db.get_address_list()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)
