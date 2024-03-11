import schedule
import time
import datetime


def say_hello():
    current_time = datetime.datetime.now()
    repetitions = min(current_time.hour + 1, 12)
    message = 'Ку' * repetitions
    print(message)


schedule.every().hour.at(":00").do(say_hello)

while True:
    schedule.run_pending()
    time.sleep(1)
