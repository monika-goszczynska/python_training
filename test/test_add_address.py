# -*- coding: utf-8 -*-
from model.address import Address
import pytest


def random_string(prefix, maxlen):
    symbols = string.digits + string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Address(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", home_telephone="", mobile_telephone="",
                    work_telephone="", fax="", email="", email2="", email3="", homepage="", birth_day="", birth_month="-", birth_year="", anni_day="",
                    anni_month="-", anni_year="", second_address="", phone2="", notes="")] + [
    Address(first_name=random_string("fname", 10), middle_name=random_string("mname", 10), last_name=random_string("lname", 10), nickname=random_string("nick", 10),
            title=random_string("title", 10), company=random_string("comp", 10), address=random_string("address", 10), home_telephone=random_string("htel", 10),
            mobile_telephone=random_string("mtel", 10), work_telephone=random_string("wtel", 10), fax=random_string("fax", 10), email=random_string("email@", 5),
            email2=random_string("email2@", 5), email3=random_string("email3@", 5), homepage=random_string("homep", 10), birth_day="1", birth_month="January", birth_year="1990", anni_day="1", anni_month="January",
                    anni_year="2000", second_address="secaddress", phone2="home", notes="notes")
]


def test_add_address(app):
    old_addresses = app.address.get_address_list()
    app.address.new(address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)



#def test_add_empty_address(app):
#    old_addresses = app.address.get_address_list()
#    address = Address(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", home_telephone="",
#                            mobile_telephone="", work_telephone="", fax="", email="", email2="", email3="",
#                            homepage="", birth_day="", birth_month="-", birth_year="", anni_day="", anni_month="-", anni_year="", second_address="", phone2="", notes="")
#    app.address.new(address)
#    new_addresses = app.address.get_address_list()
#    assert len(old_addresses) + 1 == len(new_addresses)
#    old_addresses.append(address)
#    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)