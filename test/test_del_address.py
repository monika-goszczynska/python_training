from model.address import Address


def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.new(Address(first_name="test", middle_name="test", last_name="test"))
    app.address.delete_first_address()