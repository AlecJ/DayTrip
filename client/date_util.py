"""

"""

from datetime import datetime


def prompt_time(default_time, text):
    """
    Prompt the user to input a time.

    :param default_time: String, The default time to offer
    :param text: String, The text to prompt the user with

    :return: A datetime, the current day and the user input time
    """
    while(True):
        print(text)
        help = "Specify time in HH:MM format: "
        time = input(help) or default_time

        try:
            # convert string to datetime, will be 1900-01-01
            time = datetime.strptime(time, "%H:%M")
            
            # convert datetime to today
            today = datetime.now()
            time = datetime(today.year, today.month, today.day, time.hour, time.minute)
            return time

        except:
            print("Please enter correct time in HH:MM format")
