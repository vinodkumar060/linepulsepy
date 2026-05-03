from linepulsepy import profile_lines
import time

@profile_lines
def test():
    for i in range(5):
        time.sleep(0.2)

@profile_lines
def call():
    time.sleep(2)

@profile_lines
def test_func():
    x = 0
    for i in range(5):
        call()
        x += i
        test()
        time.sleep(0.2)
    return x

test_func()