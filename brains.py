# Author: Michael Hawes
# Project Leo
# brains.py
import sys
import pyaudio
from Generics.decision import Decision
from Generics.string_ratio import Ratio
import logging


#==============PYTHON LOGGING===================================================
log = logging.getLogger(__name__)  # logs all text
logger = logging.getLogger(__name__)



#==============LEO'S BRAINS=====================================================
class Leo:

    STOP_COMMANDS = ["exit"] # commands to exit the program

    @classmethod
    def complete_action(self, command, **kwargs):  # passes a variable number to a function
        """
        executes command
        """

        command = command.lower() #converts text to lowercase for easier processing

        log.debug("COMMAND: '%s'", command) # %s inserts value into string

        if command in self.STOP_COMMANDS:
            log.info("Thank you, Have a good day!.")
            return False

        elif len(command) > 0:
            original_command = command  # stores original command to be used later
            method = Ratio.compare(self, command) # returns most relevant command (highest ratio)   ex. "search for"
            Decision.transfer(self, method, original_command)
            #speak.say(answer)
            return  # keep program running

        else:
            return


def audio_loop():
    """
    Understands speceh from user and determines command
    """
    GOOGLE_SPEECH_RECOGNITION_API_KEY = None # for testing purposes, we're just using the default API key
    import speech_recognition as sr
    import os
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                logger.debug("Say 'Leo'")
                audio = r.listen(source)
                logger.debug("Assessing user input")
                name = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
                log.debug("COMMAND: '%s'", name) # %s inserts value into string
                name_list = ['leo', 'Leo', 'rio', 'Rio']
                if name in name_list:
                    os.system('afplay /System/Library/Sounds/Sosumi.aiff')   # play beep sound to notify user
                    logger.debug("How can I help you?")
                    audio = r.listen(source)
                    logger.debug("Assessing user input")
                    try:
                        result = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)

                        Leo.complete_action(result) # DETERMINES what to do with command

                    except sr.UnknownValueError:
                        logger.debug("Could not understand audio")
                    except sr.RequestError as ex:
                        logger.warn("Could not request results: %s", ex)
                    except Exception as ex:
                        logger.error("Could not process text: %s", ex)

            except sr.UnknownValueError:
                logger.debug("Could not understand audio")
            except sr.RequestError as ex:
                logger.warn("Could not request results: %s", ex)
            except Exception as ex:
                logger.error("Could not process text: %s", ex)



def text_loop():

        while True:
            logger.debug("Type Something!")
            result = input("type something: ")

            try:
                Leo.complete_action(result) # DETERMINES what to do with command

            except Exception as ex:
                logger.error("Could not process text: %s", ex)

def main():
    # Set up logger.
    FORMAT = '%(asctime)s %(filename)s:%(lineno)s [%(levelname)s] %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    audio_loop()
    #text_loop()

if __name__ == '__main__':
    main()
