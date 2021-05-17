import pymysql.cursors
import pymysql.connections
from model.group import Group
from model.address import Address


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name.strip(), header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_address_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, phone2) = row
                list.append(Address(id=str(id), first_name=firstname, last_name=lastname, home_telephone=home,
                                    mobile_telephone=mobile, work_telephone=work, phone2=phone2))
        finally:
                cursor.close()
        return list

    def destroy(self):
        self.connection.close()
