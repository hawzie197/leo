# Author: Michael Hawes
# Project Leo
# db.py

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('leo.db')  # define connection
c = conn.cursor()  # start cursor


class Database:


    def create_table(self):
        """Create a table with specified number of columns"""
        c.execute('CREATE TABLE IF NOT EXISTS jokes(joke TEXT)')

    create_table()

    def data_entry(self):
        """Enter a single data row into database"""
        c.execute("INSERT INTO stuffToPlot VALUES('hello', 'hi how are you', '5 December 2016')")
        conn.commit()

    def dynamic_data_entry(self):
        """Enter a multi-row entry into the database"""
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        keyword = 'Python'
        value = random.randrange(0,10)
        c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
        (unix, date, keyword, value))
        conn.commit()


    def read_from_db(self, command):
        """pull data at column where value = question"""
        try:
            c.execute('SELECT value FROM stuffToPlot WHERE keyword = ?',(command,))  #populate cursor with value as tuple
            for row in c.fetchall():
                return row
        except:
            raise ValueError('{} is not a valid database keyword'.format(command))


