#!/usr/bin/python3
""" create state table in hbtn_0e_0_usa with data """
CREAT DATABASE IF EXIST hbtn_0e_0_usa;
import MySQLdb
import sys

if __name__ == __"main"__:
    db = MySQLdb.connect(host="localhost", port=3360, user=sys.argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
