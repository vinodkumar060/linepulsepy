"""Profiler Implementation"""

import sys
import time
import inspect
from functools import wraps
from .utils import Color

def profile_lines(func):
    """
    Profile execution time of each line in a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        timings = {}
        lines, start_line = inspect.getsourcelines(func)

        def trace(frame, event, arg):
            if event != "line":
                return trace

            lineno = frame.f_lineno
            start = time.perf_counter()

            def local_trace(frame, event, arg):
                elapsed = time.perf_counter() - start
                timings[lineno] = timings.get(lineno, 0) + elapsed
                return trace

            return local_trace

        sys.settrace(trace)
        result = func(*args, **kwargs)
        sys.settrace(None)

        print(f"\n{Color.YELLOW}🔍 LinePulse Report for {func.__name__}:{Color.RESET}\n")
        for idx, line in enumerate(lines):
            lineno = start_line + idx
            elapsed = timings.get(lineno, 0)

            # decide color based on time
            if elapsed > 0.3:
                color = Color.RED
            elif elapsed > 0.1:
                color = Color.YELLOW
            else:
                color = Color.GREEN

            print(f"{color}{lineno:4} | {elapsed:.6f}s | {line.rstrip()}{Color.RESET}")

        return result

    return wrapper