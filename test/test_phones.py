
def test_phones_on_address_view_page(app):
    address_from_view_page = app.address.get_address_from_view_page(0)
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_view_page.home_telephone == address_from_edit_page.home_telephone
    assert address_from_view_page.work_telephone == address_from_edit_page.work_telephone
    assert address_from_view_page.mobile_telephone == address_from_edit_page.mobile_telephone
    assert address_from_view_page.phone2 == address_from_edit_page.phone2
