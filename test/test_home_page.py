import re


def test_data_on_home_page(app):
    # info o kontakcie ze str glownej
    address_from_home_page = app.address.get_address_list()[0]
    # info o kontakcie z formy edytowania
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_home_page.first_name == address_from_edit_page.first_name
    assert address_from_home_page.last_name == address_from_edit_page.last_name
    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_edit_page)
    assert address_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(address_from_edit_page)


def clear(s):
    return re.sub('[() -]', '', s)


def merge_phones_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [address.home_telephone, address.mobile_telephone, address.work_telephone, address.phone2]))))


def merge_emails_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            (filter(lambda x: x is not None, [address.email, address.email2, address.email3]))))