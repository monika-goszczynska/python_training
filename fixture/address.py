from selenium.webdriver.support.ui import Select
from keyboard import press


class AddressHelper:

    def __init__(self, app):
        self.app = app

    def new(self, address):
        # to jest łącze do sterownika webdriver.Firefox
        wd = self.app.wd
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

    def delete_first_address(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        press('enter')

    def modify_first_address(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys('modified')
