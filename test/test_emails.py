
def test_emails_on_home_page(app):
    # info o kontakcie ze str glownej
    address_from_home_page = app.address.get_address_list()[0]
    # info o kontakcie z formy edytowania
    address_from_edit_page = app.address.get_address_info_from_edit_page(0)
    assert address_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(address_from_edit_page)


def merge_emails_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            (filter(lambda x: x is not None, [address.email, address.email2, address.email3]))))