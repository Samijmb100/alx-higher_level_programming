#!/usr/bin/python3
"""List all files in the database"""

if __name__ == "__main__":
    """ ORM script that select  and query a database using MySQL model"""

    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host = 'localhost', user = argv[1], passwd = argv[2], db = argv[3], port = 3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_row = cur.fetchall()

    for row in query_row:
        print(row)

