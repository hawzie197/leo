# Author: Michael Hawes
# Project Leo
# search.py
import time
import webbrowser
from bs4 import BeautifulSoup
import urllib.request
from subprocess import call
from Functions.date_time import DateTime
from Functions.weather import Weather
import speech_recognition as sr
import logging

log = logging.getLogger(__name__)  # logs all text
logger = logging.getLogger(__name__)

D = DateTime()
W = Weather()

class Internet:


    def open_browser(self):
        """
        opens a browser in a new tab on your computer
        """
        url = "http://www.google.com"
        webbrowser.open(url,new=2)


    def search_internet(self):
        """
        returns an answer to a question based search
        """
        GOOGLE_SPEECH_RECOGNITION_API_KEY = None # for testing purposes, we're just using the default API key
        r = sr.Recognizer()
        with sr.Microphone() as source:

            while True:
                call(["espeak", "-v", "mb-us1", "What are you curious about?"])
                try:
                    audio = r.listen(source)
                    question = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
                    call(["espeak", "-v", "mb-us1", "Let me see what I can find"])
                    url = "https://en.wikipedia.org/wiki/" +(str(question))
                    info_list = []
                    sauce = urllib.request.urlopen(url).read()   # gives us the html text
                    soup = BeautifulSoup(sauce, 'lxml')   # makes the html text pretty
                    for pi in soup.find_all('p'):  # pi is page info
                        info_list.append(pi.text)
                    para = info_list[0]
                    para = para.split('.')
                    call(["espeak", "-v", "mb-us1", para[0]])

                    call(["espeak", "-v", "mb-us1", "Would you like to know more about" + question])
                    audio = r.listen(source)
                    keep_going = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
                    count = 1
                    yes_list = ['yea','yes', 'sure', 'absolutely', 'of course', 'please', 'yee', 'yes please']
                    while keep_going.lower() in yes_list:
                        call(["espeak", "-v", "mb-us1", para[count]])
                        call(["espeak", "-v", "mb-us1", "Should I keep going?"])
                        audio = r.listen(source)
                        keep_going = r.recognize_google(audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
                        count += 1
                except sr.UnknownValueError:
                    logger.debug("Could not understand audio")
                except sr.RequestError as ex:
                    logger.warn("Could not request results: %s", ex)
                except Exception as ex:
                    logger.error("Could not process text: %s", ex)
                return False


    def get_news(self):
        """
        gets the most recent headline from bbc news
        """
        info_list = []
        sauce = urllib.request.urlopen("http://www.bbc.com/news/").read()   # gives us the html text
        soup = BeautifulSoup(sauce, 'lxml')   # makes the html text pretty

        #text = soup.find("p", "gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")    # allows you to get a specific classes paragraph

        for pi in soup.find_all('p'):  # pi is page info
            info_list.append(pi.text)

        news1,news2,news3,news4 = info_list[1],info_list[2],info_list[3],info_list[4]
        #news_update = "The first news up date is,"+ news1 + "the second update is," + news2 + "the third update is" + news3 + "the fourth update is" + news4

        call(["espeak", "-ven-us+m1", "-s170", "first update"])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", news1])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", "second update"])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", news2])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", "third update"])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", news3])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", "fourth update"])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", news4])   # returns the top 4 headings


    def get_market_update(self):
        """
        returns real time updates about how the S&P500, Nasdaq, and Dow 30 are doing
        and or did for the day
        @decision = there are two decisions allowing the data to be recorded
        """
        try:
            market_list = []
            current_time = time.strftime('%H:%M').split(':')
            current_time = current_time[0]+current_time[1]
            sauce = urllib.request.urlopen("https://finance.yahoo.com").read()   # gives us the html text
            soup = BeautifulSoup(sauce, 'lxml')   # makes the html text pretty

            #text = soup.find("p", "gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")    # allows you to get a specific classes paragraph

            for pi in soup.find_all('span', class_="Fz(xs) Fw(b) C($dataGreen)"):  # pi is page info
                market_list.append(pi.text)


            # this section declares the point change of each market
            sp500 = market_list[0].split(' ')
            sp500_point_change = sp500[0]

            dow30 = market_list[1].split(' ')
            dow30_point_change = dow30[0]

            nasdaq = market_list[2].split(' ')
            nasdaq_point_change = nasdaq[0]

            # based on whether or not the market is open, the response will be slightly different

            if int(current_time) > 1630 or int(current_time) < 930:
                call(["espeak", "-ven-us+m1", "-s170", "the market is closed with the, S AND P 500, having a" + str(sp500_point_change) + "point change, the, DOW, has a" + str(dow30_point_change) + "point change and the, NASDAQ, has a" + str(nasdaq_point_change) + "point change"])
            else:
                call(["espeak", "-ven-us+m1", "-s170", "the market is currently open with the, S AND P 500, having a" + str(sp500_point_change) + "point change, the, DOW, has a " + str(dow30_point_change) + "point change and the, NASDAQ, has a " + str(nasdaq_point_change) + "point change"])
        except:
                market_list = []
                current_time = time.strftime('%H:%M').split(':')
                current_time = current_time[0]+current_time[1]
                sauce = urllib.request.urlopen("https://finance.yahoo.com").read()   # gives us the html text
                soup = BeautifulSoup(sauce, 'lxml')   # makes the html text pretty

                #text = soup.find("p", "gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")    # allows you to get a specific classes paragraph

                for pi in soup.find_all('span', class_="Fz(xs) Fw(b) C($dataRed)"):  # pi is page info
                    market_list.append(pi.text)


                # this section declares the point change of each market
                sp500 = market_list[0].split(' ')
                sp500_point_change = sp500[0]

                dow30 = market_list[1].split(' ')
                dow30_point_change = dow30[0]

                nasdaq = market_list[2].split(' ')
                nasdaq_point_change = nasdaq[0]

                # based on whether or not the market is open, the response will be slightly different
                if int(current_time) > 1630 or int(current_time) < 930:
                    call(["espeak", "-ven-us+m1", "-s170", "the market is closed with the, S AND P 500, having a" + str(sp500_point_change) + "point change, the, DOW, has a" + str(dow30_point_change) + "point change and the, NASDAQ, has a" + str(nasdaq_point_change) + "point change"])
                else:
                    call(["espeak", "-ven-us+m1", "-s170", "the market is currently open with the, S AND P 500, having a" + str(sp500_point_change) + "point change, the, DOW, has a " + str(dow30_point_change) + "point change and the, NASDAQ, has a " + str(nasdaq_point_change) + "point change"])

    def get_sports_news_update(self):
        """
        returns the latest headlines in the sports industry
        """
        info_list = []
        sauce = urllib.request.urlopen("http://www.usatoday.com/sports/").read()   # gives us the html text
        soup = BeautifulSoup(sauce, 'lxml')   # makes the html text pretty

        #text = soup.find("p", "gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")    # allows you to get a specific classes paragraph

        for pi in soup.find_all('span', class_="js-asset-headline js-asset-headline-short placeholder-hide"):  # pi is page info
            info_list.append(pi.text)

        news1,news2,news3,news4 = info_list[0],info_list[1],info_list[2],info_list[3]
        #news_update = "The first news up date is,"+ news1 + "the second update is," + news2 + "the third update is" + news3 + "the fourth update is" + news4

        call(["espeak", "-ven-us+m1", "-s170", "first update"])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", news1])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", "second update"])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", news2])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", "third update"])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", news3])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", "fourth update"])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", news4])   # returns the top 4 headings

    def whats_up(self):
        call(["espeak", "-ven-us+m1", "-s170", "Hello and Good afternoon!"])   # returns the top 4 headings
        dt = D.get_datetime()
        w = W.get_weather()  # add city code (to find, go to json file and look up code)
        info_list = []
        sauce = urllib.request.urlopen("http://www.bbc.com/news/").read()   # gives us the html text
        soup = BeautifulSoup(sauce, 'lxml')   # makes the html text pretty

        #text = soup.find("p", "gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")    # allows you to get a specific classes paragraph

        for pi in soup.find_all('p'):  # pi is page info
            info_list.append(pi.text)

        news1,news2,news3,news4 = info_list[1],info_list[2],info_list[3],info_list[4]
        #news_update = "The first news up date is,"+ news1 + "the second update is," + news2 + "the third update is" + news3 + "the fourth update is" + news4
        call(["espeak", "-ven-us+m1", "-s170", "Here's a quick news update!"])   # returns the top 4 headings
        call(["espeak", "-ven-us+m1", "-s170", news1])   # returns the top 4 headings
    #
    # def get_nfl_news_update():
    #     """
    #     gets the most recent nfl headlines from cbs sports
    #     """
    #     info_list = []
    #     sauce = urllib.request.urlopen("https://twitter.com/MySportsUpdate?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor").read()   # gives us the html text
    #     soup = BeautifulSoup(sauce, 'lxml')   # makes the html text pretty
    #
    #     #text = soup.find("p", "gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")    # allows you to get a specific classes paragraph
    #     for pi in soup.find_all('li', class_="js-stream-item stream-item stream-item "):
    #         info_list.append(pi.text)
    #     print(info_list[len(info_list-5)]:)
    #
    #
    # def get_nba_news_update():
    #     pass
