from model.address import Address


def test_modify_first_name(app):
    if app.address.count() == 0:
        app.address.new(Address(first_name="test", middle_name="test", last_name="test"))
    app.address.modify_first_address(Address(first_name="New first name"))


def test_modify_bday(app):
    if app.address.count() == 0:
        app.address.new(Address(first_name="test", middle_name="test", last_name="test"))
    app.address.modify_first_address(Address(birth_day="6"))
