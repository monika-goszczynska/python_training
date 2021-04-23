
def test_phones_on_home_page(app):
    address_from_home_page = app.address.get_address_list()[0]
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_home_page.home_telephone == address_from_edit_page.home_telephone
    assert address_from_home_page.work_telephone == address_from_edit_page.work_telephone
    assert address_from_home_page.mobile_telephone == address_from_edit_page.mobile_telephone
    assert address_from_home_page.home == address_from_edit_page.home