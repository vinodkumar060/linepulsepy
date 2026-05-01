from linepulsepy import profile_lines
import time


def call():
    time.sleep(2)

@profile_lines
def test_func():
    x = 0
    for i in range(5):
        call()
        x += i
        time.sleep(0.2)
    return x

test_func()