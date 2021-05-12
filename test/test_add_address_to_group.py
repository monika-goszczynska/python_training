from model.address import Address
from model.group import Group


def add_address_to_group(app, db):
    address = db.get_address_list()
    group = db.get_group_list()