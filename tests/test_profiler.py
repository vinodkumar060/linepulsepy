"""Test Profiler Implementation"""


from linepulsepy import profile_lines
import time

@profile_lines
def sample():
    x = 0
    for i in range(3):
        x += i
        time.sleep(0.1)
    return x


def test_sample():
    result = sample()
    assert result == 3