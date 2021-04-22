from model.address import Address


def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.new(Address(first_name="test", middle_name="test", last_name="test"))
    old_addresses = app.address.get_address_list()
    app.address.delete_first_address()
    # assert len(old_addresses) - 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses[0:1] = []
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)