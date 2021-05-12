from model.address import Address


def test_address_on_home_page(app):
    # info o kontakcie ze str glownej
    address_from_home_page = app.address.get_address_list()[0]
    # info o kontakcie z formy edytowania
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_home_page.address == merge_address_like_on_home_page(address_from_edit_page)


def test_addresses_on_home_page(app, db):
    addresses_from_db = db.get_address_list()
    addresses_from_home_page = app.address.get_address_list()
    assert sorted(addresses_from_db, key=Address.id_or_max) == sorted(addresses_from_home_page, key=Address.id_or_max)


def merge_address_like_on_home_page(address):
    return "\n".join([address.address])