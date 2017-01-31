# Author: Michael Hawes
# Date: 28 December 2016
# Project Leo
# toDoList.py

import speech_recognition as sr
from subprocess import call
import logging
import sqlite3
log = logging.getLogger(__name__)  # logs all text
logger = logging.getLogger(__name__)
conn = sqlite3.connect('leo.db')  # define connection
c = conn.cursor()  # start cursor

class Tasks:

    def add_task(self):
        """
        Adds a task to the database
        """
        GOOGLE_SPEECH_RECOGNITION_API_KEY = None # for testing purposes, we're just using the default API key
        r = sr.Recognizer()
        with sr.Microphone() as source:
            task = None
            while task == None:
                call(["espeak", "-v", "mb-us1", "Okay, what would you like to add?"])
                audio = r.listen(source)
                try:
                    task = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
                    call(["espeak", "-v", "mb-us1", task + ',' + "has been added to your todo list"])
                    c.execute("INSERT INTO toDoList VALUES(?)",(task,))
                    conn.commit()
                except sr.UnknownValueError:
                    logger.debug("Could not understand audio")
                except sr.RequestError as ex:
                    logger.warn("Could not request results: %s", ex)
                except Exception as ex:
                    logger.error("Could not process text: %s", ex)

    def remove_task(self):
        """
        Removes a task from the database
        """
        GOOGLE_SPEECH_RECOGNITION_API_KEY = None # for testing purposes, we're just using the default API key
        r = sr.Recognizer()
        with sr.Microphone() as source:
            task = None
            while task == None:
                call(["espeak", "-v", "mb-us1", "Okay, what task would you like to remove?"])
                audio = r.listen(source)
                try:
                    task = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
                    call(["espeak", "-v", "mb-us1", task + ',' + "has been removed from your todo list"])
                    c.execute('DELETE FROM toDoList WHERE task=?', (task,))
                    conn.commit()
                except sr.UnknownValueError:
                    logger.debug("Could not understand audio")
                except sr.RequestError as ex:
                    logger.warn("Could not request results: %s", ex)
                except Exception as ex:
                    logger.error("Could not process text: %s", ex)


    def read_tasks(self):
        """
        returns a list of all tasks in the database
        """
        try:
            call(["espeak", "-v", "mb-us1", "Your tasks are as follows"])
            c.execute('SELECT * FROM toDoList')  #populate cursor with value as tuple
            for row in c.fetchall():
                call(["espeak", "-v", "mb-us1", str(row)])
        except:
            raise ValueError('No values in todo list')


    def num_tasks(self):
        """
        returns the number of tasks in the to do list
        """
        tasks = []
        try:
            c.execute('SELECT * FROM toDoList')  #populate cursor with value as tuple
            for row in c.fetchall():
                tasks.append(row)
            return "you currently have",len(tasks), "tasks to complete on your list"
        except:
            raise ValueError('Could not read from database')
