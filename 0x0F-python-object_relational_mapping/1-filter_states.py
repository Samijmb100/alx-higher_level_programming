#!/usr/bin/python3

""" A basic python script that sends query to database without ORM"""

import MySQLdb
from sys import argv

if __name__ = "__main__":
    """ Access to the database and get the states
        from the """
    
    db = MySQLdb.connect(hostname = "localhost", user = argv[1], port = 3306, passwd = argv[2], db = argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE states.name LIKE 'N%'\
            ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

