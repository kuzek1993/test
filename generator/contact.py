import jsonpickle
import random
import string
from model.contact import Contact
import os.path


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(first_name=first_name, last_name=last_name,
                    mobilephone=mobilephone)
     for first_name in ["", random_string("first_name", 10)]
     for last_name in ["", random_string("last_name", 10)]
     for mobilephone in ["", random_string("mobilephone", 10)]]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json",)

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))