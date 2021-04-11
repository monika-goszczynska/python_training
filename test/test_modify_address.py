from model.address import Address


def test_modify_first_name(app):
    app.session.login(username="admin", password="secret")
    app.address.modify_first_address(Address(first_name="New first name"))
    app.session.logout()


def test_modify_bday(app):
    app.session.login(username="admin", password="secret")
    app.address.modify_first_address(Address(birth_day="20"))
    app.session.logout()
