# -*- coding: utf-8 -*-
import pytest
from model.address import Address
from fixture.application import Application


# inicjalizator fikstury
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_address(app):
    app.session.login(username="admin", password="secret")
    app.address.new(Address(first_name="fname", middle_name="mname", last_name="lname", nickname="nickname", title="title", company="company", address="address", home_telephone="hometel",
                            mobile_telephone="mobtel", work_telephone="worktel", fax="faxtel", email="email@email.com", email2="email2@email.com", email3="email3@email.com",
                            homepage="homepage", birth_day="1", birth_month="January", birth_year="1990", anni_day="1", anni_month="January", anni_year="2000", second_address="secaddress", home="home", notes="notes"))
    app.session.logout()


def test_add_empty_address(app):
    app.session.login(username="admin", password="secret")
    app.address.new(Address(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", home_telephone="",
                            mobile_telephone="", work_telephone="", fax="", email="", email2="", email3="",
                            homepage="", birth_day="", birth_month="-", birth_year="", anni_day="", anni_month="-", anni_year="", second_address="", home="", notes=""))
    app.session.logout()
