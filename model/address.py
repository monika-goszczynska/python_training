# -*- coding: utf-8 -*-
from sys import maxsize


class Address:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None,
                        address=None, all_phones_from_home_page=None, home_telephone=None, mobile_telephone=None, work_telephone=None, fax=None,
                        all_emails_from_home_page = None, email=None, email2=None, email3=None, homepage=None, birth_day=None, birth_month=None,
                        birth_year=None, anni_day=None, anni_month=None, anni_year=None, second_address=None,
                        phone2=None, notes=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_telephone = home_telephone
        self.mobile_telephone = mobile_telephone
        self.work_telephone = work_telephone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anni_day = anni_day
        self.anni_month = anni_month
        self.anni_year = anni_year
        self.second_address = second_address
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

        # ta funkcja okresla jak bedzie wygladac obiekt przy wyprowadzeniu na konsole - representation
    def __repr__(self):
        return "%s:%s" % (self.id, self.last_name)

        # biezacy obiekt self jest porownywany z innym obiektem, ktory jest przyjmowany jako parametr
        # nastepuje porownanie wg sensu, a nie fizycznego rozmieszczenia obiektow
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.last_name is None or other.last_name is None or self.last_name == other.last_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize