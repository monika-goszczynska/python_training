import re


def test_phones_on_home_page(app):
    # info o kontakcie ze str glownej
    address_from_home_page = app.address.get_address_list()[0]
    # info o kontakcie z formy edytowania
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_edit_page)


def test_phones_on_address_view_page(app):
    address_from_view_page = app.address.get_address_from_view_page(0)
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_view_page.home_telephone == address_from_edit_page.home_telephone
    assert address_from_view_page.work_telephone == address_from_edit_page.work_telephone
    assert address_from_view_page.mobile_telephone == address_from_edit_page.mobile_telephone
    assert address_from_view_page.phone2 == address_from_edit_page.phone2


def clear(s):
    return re.sub('[() -]', '', s)


def merge_phones_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [address.home_telephone, address.mobile_telephone, address.work_telephone, address.phone2]))))
