from selenium.webdriver.support.ui import Select
from model.address import Address

class AddressHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_date_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_address_form(self, address):
        wd = self.app.wd
        self.change_field_value("firstname", address.first_name)
        self.change_field_value("middlename", address.middle_name)
        self.change_field_value("lastname", address.last_name)
        self.change_field_value("nickname", address.nickname)
        self.change_field_value("title", address.title)
        self.change_field_value("company", address.company)
        self.change_field_value("address", address.address)
        self.change_field_value("home", address.home)
        self.change_field_value("mobile", address.mobile_telephone)
        self.change_field_value("work", address.work_telephone)
        self.change_field_value("fax", address.fax)
        self.change_field_value("email", address.email)
        self.change_field_value("email2", address.email2)
        self.change_field_value("email3", address.email3)
        self.change_field_value("homepage", address.homepage)
        self.change_date_value("bday", address.birth_day)
        self.change_date_value("bmonth", address.birth_month)
        self.change_field_value("byear", address.birth_year)
        self.change_date_value("aday", address.anni_day)
        self.change_date_value("amonth", address.anni_month)
        self.change_field_value("ayear", address.anni_year)
        self.change_field_value("address2", address.second_address)
        self.change_field_value("phone2", address.home)
        self.change_field_value("notes", address.notes)

    def new(self, address):
        # to jest łącze do sterownika webdriver.Firefox
        wd = self.app.wd
        # init address creation
        wd.find_element_by_link_text("add new").click()
        self.fill_address_form(address)
        # submit address creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_home_page()
        self.address_cache = None

    def select_first_address(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_address_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_address(self):
        self.delete_address_by_index(0)

    def delete_address_by_index(self, index):
        wd = self.app.wd
        self.select_address_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_home_page()
        self.address_cache = None

    def modify_first_address(self):
        self.modify_address_by_index(0)

    def modify_address_by_index(self, index, new_address_data):
        wd = self.app.wd
        self.select_address_by_index(index)
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_address_form(new_address_data)
        # submit modification
        wd.find_element_by_name("update").click()
        # wd.switch_to_alert().accept()
        self.open_home_page()
        self.address_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    address_cache = None

    def get_address_list(self):
        if self.address_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.address_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                last_name = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.address_cache.append(Address(last_name=last_name, id=id))
        # zwracana jest kopia cache
        return list(self.address_cache)
