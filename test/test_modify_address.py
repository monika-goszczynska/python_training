from model.address import Address


def test_modify_first_name(app):
    app.address.modify_first_address(Address(first_name="New first name"))


def test_modify_bday(app):
    app.address.modify_first_address(Address(birth_day="6"))
