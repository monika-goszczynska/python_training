# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.address import AddressHelper


class Application:

    def __init__(self, browser="firefox"):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        # pomocnik uzyskuje odsyłacz do obiektu klasy Application
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.address = AddressHelper(self)

    def is_valid(self):
        # blok z przechwyceniem wyjatkow
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def destroy(self):
        self.wd.quit()
