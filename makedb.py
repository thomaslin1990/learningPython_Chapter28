# FIle makedb.py store person objects on a shelve databas

from PersonExample import Person, Manager

bob = Person("Bob Smith")
sue = Person("Sue Jones", job='dev', pay=10000)
tom = Manager("Tom Jones", 50000)

import shelve
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()