# Author: Michael Hawes
# Project Leo
# send_message.py

#==============Imports==========================================================
from twilio.rest import TwilioRestClient
from subprocess import call
import logging
import speech_recognition as sr
log = logging.getLogger(__name__)  # logs all text
logger = logging.getLogger(__name__)

#==============TWILIO ESSENTIALS================================================
#api_key = open('api_key.txt','r').readline().strip()
#sid = open('sid.txt','r').readline().strip()
api_key = 'ACfe712cf8d40a3051dbcb283ada0b348e'
sid = 'ed3171d5762363af48af7c6361f4563a'
client = TwilioRestClient(api_key, sid)

class Message:


    def send_text():
        """Sends a text to chosen person based off input number"""
        #text = input('Message: ')
        #toNumber = input('Enter the number to send to: ')

        GOOGLE_SPEECH_RECOGNITION_API_KEY = None # for testing purposes, we're just using the default API key
        r = sr.Recognizer()
        with sr.Microphone() as source:
            message = None
            number = None
            while message == None and number == None:
                call(["espeak", "-v", "mb-us1", "Okay, what's the message?"])
                audio = r.listen(source)
                try:
                    message = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
                except sr.UnknownValueError:
                    logger.debug("Could not understand audio")
                except sr.RequestError as ex:
                    logger.warn("Could not request results: %s", ex)
                except Exception as ex:
                    logger.error("Could not process text: %s", ex)
                call(["espeak", "-v", "mb-us1", "Who would you like to send your message to?"])
                number_audio = r.listen(source)
                try:
                    people = {"kevin":"(413) 355-0754", "tony":"(413) 204-5213", "eddie":"(603) 494-9816", "andy":"(603) 370-8543", "dad":"(603) 418-5784", "mom":"(603) 370-8544", "kristen":"(774) 888-8884", "mike":"(603) 370-8546"}
                    person = r.recognize_google(number_audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
                    if person.lower() in people:
                        call(["espeak", "-v", "mb-us1", "Sending Message"])
                    else:
                        call(["espeak", "-v", "mb-us1", "There is no one in your contacts by the name" + ',' + person])
                    person = people[person.lower()]
                except sr.UnknownValueError:
                    logger.debug("Could not understand audio")
                except sr.RequestError as ex:
                    logger.warn("Could not request results: %s", ex)
                except Exception as ex:
                    logger.error("Could not process text: %s", ex)

        fromNumber = '(413) 207-9236'

        client.messages.create(to=person, from_=str(fromNumber) , body=str(message))



    # def send_mail(FROM,TO,SUBJECT,TEXT):
    #     import textwrap
    #     import smtplib
    #     """this is some test documentation in the function"""
    #     message = textwrap.dedent("""\
    #         From: %s
    #         To: %s
    #         Subject: %s
    #         %s
    #         """ % (FROM, ", ".join(TO), SUBJECT, TEXT))
    #     # Send the mail
    #     server = smtplib.SMTP("smtp.gmail.com", 587)
    #     server.sendmail(FROM, TO, message)
    #     server.quit()
    # send_mail('mhawes24@gmail.com', 'mh351681@wne.edu', 'test', 'sending email with python')
