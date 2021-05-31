from model.address import Address
from model.group import Group
from random import randrange


def add_address_to_group(app, db):
    address_on_home_page = app.address.get_address_list()