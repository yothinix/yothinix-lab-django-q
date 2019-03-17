import random
import time


def process_something():
    delay = random.randint(1, 10)
    print(f'delay is {delay}')
    time.sleep(delay)
    return {'amount': delay}
