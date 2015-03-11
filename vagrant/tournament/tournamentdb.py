#!/usr/bin/env python
# 
# tournamentdb.py -- Database operations used for CRUD
#

# import psycopg2 library
import psycopg2

# Database CRUD
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteAll(table):
    """Gets the db cursor and deletes all data from table given as argument."""
    db = connect()
    c = db.cursor()
    c.execute("""DELETE FROM """+table+""" *""")
    db.commit()
    db.close()

def fetchAll(table):
    """Gets the db cursor and returns all data from table given as argument."""
    db = connect()
    c = db.cursor()
    c.execute("""SELECT * FROM """+table)
    data = c.fetchall()
    db.close()
    return data

def insertRecord(table, columns, data):
    """Gets the db cusor and inserts one row of data into the table.
    Both table, affected columns and data need to be provided as arguments.
    
    Args:
      table: name of the table, string
      columns: array of column name strings
      data: a list of tuples representing the data to insert into the table
    """
    db = connect()
    c = db.cursor()

    i = 0
    for col in data:
        c.execute('INSERT INTO '+table+' ('+columns[i]+') VALUES (%s)', (col,))
        i = i+1

    db.commit()
    db.close()

def getById(table, id):
    """Gets the db cursor and returns one row by id from table given as argument
    table -> string
    id -> integer
    """
    db = connect()
    c = db.cursor()
    c.execute('SELECT * FROM players WHERE players.id = %s', (id, ))
    row = c.fetchone()
    db.close()
    return row