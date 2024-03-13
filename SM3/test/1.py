import datetime

def say_hello():
    current_time = datetime.datetime.now()
    repetitions = int(current_time.strftime("%I"))
    message = 'Ку' * repetitions
    print(message)


