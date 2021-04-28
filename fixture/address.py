from selenium.webdriver.support.ui import Select
import re
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
        self.change_field_value("home", address.home_telephone)
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
        self.change_field_value("phone2", address.phone2)
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
        self.open_address_to_edit_by_index(index)
        self.fill_address_form(new_address_data)
        # submit modification
        wd.find_element_by_name("update").click()
        # wd.switch_to_alert().accept()
        self.open_home_page()
        self.address_cache = None

    def open_address_to_edit_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        edit_cell = row.find_elements_by_tag_name("td")[7]
        # open modification form
        edit_cell.find_element_by_tag_name("a").click()


    def open_address_view_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
        view_cell = row.find_elements_by_tag_name("td")[6]
        # open view details
        view_cell.find_element_by_tag_name("a").click()

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
                first_name = cells[2].text
                last_name = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.address_cache.append(Address(last_name=last_name, first_name=first_name, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        # zwracana jest kopia cache
        return list(self.address_cache)

    def get_address_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_address_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        # to jest ukryte pole w przegladarce
        id = wd.find_element_by_name("id").get_attribute("value")
        home_telephone = wd.find_element_by_name("home").get_attribute("value")
        work_telephone = wd.find_element_by_name("work").get_attribute("value")
        mobile_telephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Address(first_name=first_name, last_name=last_name, id=id,
                       home_telephone=home_telephone, mobile_telephone=mobile_telephone,
                       work_telephone=work_telephone, phone2=phone2, email=email,
                       email2=email2, email3=email3)

    def get_address_from_view_page(self, index):
        wd = self.app.wd
        self.open_address_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_telephone = re.search("H: (.*)", text).group(1)
        work_telephone = re.search("W: (.*)", text).group(1)
        mobile_telephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Address(home_telephone=home_telephone, mobile_telephone=mobile_telephone,
                       work_telephone=work_telephone, phone2=phone2)

