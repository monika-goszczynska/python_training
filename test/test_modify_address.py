
def test_modify_first_address(app):
    app.session.login(username="admin", password="secret")
    app.address.modify_first_address()
    app.session.logout()
