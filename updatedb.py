# FIle updatedb.py: update Person object on databse

import shelve
db = shelve.open('persondb')

for key in sorted(db):
    print(key, '=>', db[key])

sue = db['Sue Jones']
sue.giveRaise(0.10)
db['Sue Jones'] = sue
db.close()