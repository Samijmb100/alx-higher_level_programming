#!/usr/bin/python3
#List all files in the database
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    usr = argv[0]
    psw = argv[1]
    dlb = argv[2]

    conn = MySQLdb.connect( user = usr, passwd = pwd, db = dlb)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_row = cur.fetchall()

    for row in query_row:
        print(row)

