import random
import string
from model.group import Group

testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2"),
    Group(name="name3", header="header3", footer="footer3"),
]



#def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    #return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata = [
            #Group(name=name, header=header, footer=footer)
            #for name in ["", random_string("name", 10)]
            #for header in ["", random_string("header", 20)]
            #for footer in ["", random_string("footer", 20)]
    #]

