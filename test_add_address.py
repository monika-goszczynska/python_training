# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddAddress(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_address(self):
        wd = self.wd
        #open home page
        wd.get("http://localhost:8080/addressbook/")
        #login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        #init address creation
        wd.find_element_by_link_text("add new").click()
        #fill in address form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("fname")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("mname")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("lname")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("nickname")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("company")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("address")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("hometel")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("mobtel")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("worktel")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("faxtel")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email@email.com")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("email2@email.com")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("email3@email.com")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("homepage")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("January")
        wd.find_element_by_xpath("(//option[@value='January'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("secaddress")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("home")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("notes")
        #submit address creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        #logout
        wd.find_element_by_link_text("Logout").click()
    
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
