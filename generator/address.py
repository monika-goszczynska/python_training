from model.address import Address
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of addresses", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/addresses.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.digits + string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Address(first_name="", middle_name="", last_name="", nickname="", title="",
            company="", address="", home_telephone="", mobile_telephone="", work_telephone="",
            fax="", email="", email2="", email3="", homepage="", birth_day="",
            birth_month="-", birth_year="", anni_day="", anni_month="-", anni_year="",
            second_address="", phone2="", notes="")] + [
    Address(first_name=random_string("fname", 10), middle_name=random_string("mname", 10), last_name=random_string("lname", 10),
            nickname=random_string("nick", 5), title=random_string("title", 5), company=random_string("comp", 6),
            address=random_string("addr", 10), home_telephone=random_string("htel", 4),
            mobile_telephone=random_string("mtel", 4), work_telephone=random_string("wtel", 4),
            fax=random_string("fax", 4), email=random_string("email@", 5), email2=random_string("email2@", 5),
            email3=random_string("email3@", 5), homepage=random_string("hpage", 4), birth_day="", birth_month="-",
            birth_year="", anni_day="", anni_month="-", anni_year="", second_address=random_string("addr2", 6),
            phone2=random_string("phone2", 4), notes=random_string("notes", 10))
    for i in range(n)
]


# zachowanie generowanych danych do pliku
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
