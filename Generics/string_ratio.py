# Author: Michael Hawes
# Project Leo
# string_ratio.py

from fuzzywuzzy import fuzz
#from fuzzywuzzy import process
import sqlite3


conn = sqlite3.connect('leo.db')  # define connection
c = conn.cursor()  # start cursor

class Ratio:

    def compare(self, command):
        """
        fuzzywuzzy determines a string ratio. We use that ratio to determine
        which operation to carry out for the command.
        """

        table_list = {}

        c.execute('SELECT * FROM commands;')  # populate cursor with value as tuple
        for row in c.fetchall():
            row = str(row)
            ratio = fuzz.ratio(str(command), row)
            row = row.lstrip('(').rstrip(')').rstrip(',').rstrip("'").lstrip("'")
            table_list[str(ratio)] = row

        return table_list[max(table_list)] # we want the max ratio to determine most accurate operation
