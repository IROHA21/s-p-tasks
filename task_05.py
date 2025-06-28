

import time


def date_in_future(integer):
    current_timestamp = int(time.time())

    if not integer:
        return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(current_timestamp))

    future_timestamp = current_timestamp + (integer * 86400)
    return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(future_timestamp))




print(date_in_future([])) # => текущая дата
print(date_in_future(2))  # => текущая дата + 2 дня