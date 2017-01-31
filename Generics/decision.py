from Functions.weather import Weather
from Functions.calculator import Math
from Functions.task_list import Tasks
from Functions.joke_page import Jokes
from Functions.search import Internet
from Functions.send_message import Message
from Functions.date_time import DateTime

D = DateTime()
W = Weather
J = Jokes()
I = Internet()
M = Message()
MA = Math()
T = Tasks()


class Decision:


    def transfer(self, method, original_command):
        """
        transfer sends the original command to specified method
        """
        try:

            if method == "whats up":
                I.whats_up()
                return

            if method == "tell me a joke":
                J.tell_joke()
                return

            elif method == "add task":
                T.add_task()
                return

            elif method == "remove task" or method == "delete task":
                T.remove_task()
                return

            elif method == "do I have any tasks in my list":
                T.read_tasks()
                return

            elif method == "calculate":
                MA.math(original_command)
                return

            elif method == "what time is it":
                D.get_time()
                return

            elif method == "what is the date":
                D.get_date()
                return

            elif method == "how is the weather":
                W.get_weather()
                return

            elif method == "send text message":
                M.send_text()
                return

            elif method == "tell me the news":
                I.get_news()
                return

            elif method == "update me on sports":
                I.get_sports_news_update()
                return

            elif method == "open browser":
                I.open_browser()
                return

            elif method == "How is the stock market today":
                I.get_market_update()
                return

            elif method == "I am curious about something":
                I.search_internet()
                return

            # # end of completed actions
            #
            # elif method == "look up":
            #     if "look up" in original_command:
            #         original_command -= "look up"
            #         return search.search_internet(original_command)
            #
            # elif method == "search for":
            #     if "search for" in original_command:
            #         original_command -= "search for"
            #         return search.search_internet(original_command)  # searches the internet
            #
            # elif method == "find":
            #     if "find" in original_command:
            #         original_command -= "find"
            #         return search.search_internet(original_command)
            #
            # elif method == "how does":
            #     return search.search_internet(original_command)
            #
            # elif method == "how do":
            #     return search.search_internet(original_command)
            #
            # elif method == "how does":
            #     return search.search_internet(original_command)
            #
            # elif method == "how far is":
            #     return search.search_internet(original_command)


            else:
                return

        except:
            raise ValueError("No matching commands")
