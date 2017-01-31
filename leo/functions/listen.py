from leo import Leo

import logging
import speech_recognition as sr

logger = logging.getLogger(__name__)

# for testing purposes, we're just using the default API key
GOOGLE_SPEECH_RECOGNITION_API_KEY = None

def audio_loop():
    # Most of this code taken from https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py.
    r = sr.Recognizer()
    with sr.Microphone() as source:

        while True:
            logger.debug("Say Something!")
            audio = r.listen(source)

            logger.debug("Assessing user input")

            try:
                result = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)

                Leo.complete_action(speech) #jumpts over to leo.py and method complete_action()


            except sr.UnknownValueError:
                logger.debug("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                logger.warn("Could not request results from Google Speech Recognition service: %s", e)
            except Exception as e:
                logger.error("Could not process text: %s", e)

def main():
    # Set up logger.
    FORMAT = '%(asctime)s %(filename)s:%(lineno)s [%(levelname)s] %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    audio_loop()

if __name__ == '__main__':
    main()
