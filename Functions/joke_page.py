# Author : Michael Hawes
# Date: 2 January 2017
# Project Leo
# joke_page.py
from random import randint
import speech_recognition as sr
from subprocess import call
import logging
import sqlite3

log = logging.getLogger(__name__)  # logs all text
logger = logging.getLogger(__name__)
conn = sqlite3.connect('leo.db')  # define connection
c = conn.cursor()  # start cursor

class Jokes:
    
    def tell_joke(self):
        """
        tells a random joke from database
        """
        joke_list = []
        rand_int = randint(0,20)
        try:
            c.execute('SELECT * FROM jokes')  #populate cursor with value as tuple
            for row in c.fetchall():
                joke_list.append(row)

            call(["espeak", "-v", "mb-us1", str(joke_list[rand_int])])
        except sr.UnknownValueError:
            logger.debug("Could not understand audio")
        except sr.RequestError as ex:
            logger.warn("Could not request results: %s", ex)
        except Exception as ex:
            logger.error("Could not process text: %s", ex)
