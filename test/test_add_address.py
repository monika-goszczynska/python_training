# -*- coding: utf-8 -*-
from model.address import Address


def test_add_address(app):
    old_addresses = app.address.get_address_list()
    app.address.new(Address(first_name="fname", middle_name="mname", last_name="lname", nickname="nickname", title="title", company="company", address="address", home_telephone="hometel",
                            mobile_telephone="mobtel", work_telephone="worktel", fax="faxtel", email="email@email.com", email2="email2@email.com", email3="email3@email.com",
                            homepage="homepage", birth_day="1", birth_month="January", birth_year="1990", anni_day="1", anni_month="January", anni_year="2000", second_address="secaddress", home="home", notes="notes"))
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) + 1 == len(new_addresses)


def test_add_empty_address(app):
    old_addresses = app.address.get_address_list()
    app.address.new(Address(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", home_telephone="",
                            mobile_telephone="", work_telephone="", fax="", email="", email2="", email3="",
                            homepage="", birth_day="", birth_month="-", birth_year="", anni_day="", anni_month="-", anni_year="", second_address="", home="", notes=""))
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) + 1 == len(new_addresses)
