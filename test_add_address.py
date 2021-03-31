# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from address import Address

class TestAddAddress(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_address(self):
        #to jest łącze do sterownika webdriver.Firefox
        wd = self.wd
        self.open_home_page(wd)#could we also import existing methods from test_add_group?
        self.login(wd, username="admin", password="secret")
        #could we also create a separate class for eg. birthdate and anniversary date? And then use more than 1 object as parameter?
        self.add_new_address(wd, Address(first_name="fname", middle_name="mname", last_name="lname", nickname="nickname", title="title", company="company", address="address", home_telephone="hometel",
                             mobile_telephone="mobtel", work_telephone="worktel", fax="faxtel", email="email@email.com", email2="email2@email.com", email3="email3@email.com",
                             homepage="homepage", birth_day="1", birth_month="January", birth_year="1990", anni_day="1", anni_month="January", anni_year="2000", second_address="secaddress", home="home", notes="notes"))
        self.logout(wd)

    def test_add_empty_address(self):
        #to jest łącze do sterownika webdriver.Firefox
        wd = self.wd
        self.open_home_page(wd)#could we also import existing methods from test_add_group?
        self.login(wd, username="admin", password="secret")
        self.add_new_address(wd, Address(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", home_telephone="",
                             mobile_telephone="", work_telephone="", fax="", email="", email2="", email3="",
                             homepage="", birth_day="", birth_month="-", birth_year="", anni_day="", anni_month="-", anni_year="", second_address="", home="", notes=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_new_address(self, wd, address):
        # init address creation
        wd.find_element_by_link_text("add new").click()
        # fill in address form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(address.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(address.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(address.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(address.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(address.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(address.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(address.home_telephone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(address.mobile_telephone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(address.work_telephone)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(address.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(address.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(address.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(address.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(address.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(address.birth_day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(address.birth_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(address.birth_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(address.anni_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(address.anni_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(address.anni_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address.second_address)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(address.home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(address.notes)
        # submit address creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost:8080/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
