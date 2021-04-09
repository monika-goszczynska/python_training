from selenium.webdriver.support.ui import Select


class AddressHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

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
        # change all dates!!!
        self.change_field_value("bday", address.birth_day)
        self.change_field_value("bmonth", address.birth_month)
        self.change_field_value("byear", address.birth_year)
        self.change_field_value("aday", address.anni_day)
        self.change_field_value("amonth", address.anni_month)
        self.change_field_value("ayear", address.anni_year)
        self.change_field_value("address2", address.second_address)
        self.change_field_value("phone2", address.home)
        self.change_field_value("notes", address.notes)
        # wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text(address.birth_day)
        # wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text(address.birth_month)
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys(address.birth_year)
        # wd.find_element_by_name("aday").click()
        # Select(wd.find_element_by_name("aday")).select_by_visible_text(address.anni_day)
        # wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text(address.anni_month)
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        # wd.find_element_by_name("ayear").send_keys(address.anni_year)

    def new(self, address):
        # to jest łącze do sterownika webdriver.Firefox
        wd = self.app.wd
        # init address creation
        wd.find_element_by_link_text("add new").click()
        self.fill_address_form(address)
        # submit address creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def select_first_address(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_address(self):
        wd = self.app.wd
        self.select_first_address()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def modify_first_address(self, new_address_data):
        wd = self.app.wd
        self.select_first_address()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_address_form(new_address_data)
        # submit modification
        wd.find_element_by_name("update").click()
        # wd.switch_to_alert().accept()
