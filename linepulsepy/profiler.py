"""Profiler Implementation"""

import sys
import time
import inspect
from functools import wraps
from .utils import Color

def profile_lines(func):
    """
    Profile execution time of each line in a function.
    Handles nested profiled functions correctly.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        timings = {}
        lines, start_line = inspect.getsourcelines(func)

        # Track last executed line + timestamp per frame
        frame_state = {}

        def trace(frame, event, arg):
            # Only trace THIS function
            if frame.f_code != func.__code__:
                return trace

            if event == "call":
                frame_state[frame] = {
                    "last_time": time.perf_counter(),
                    "last_line": frame.f_lineno,
                }
                return trace

            if event == "line":
                state = frame_state.get(frame)
                if state:
                    now = time.perf_counter()
                    elapsed = now - state["last_time"]

                    lineno = state["last_line"]
                    timings[lineno] = timings.get(lineno, 0) + elapsed

                    # update state
                    state["last_time"] = now
                    state["last_line"] = frame.f_lineno

                return trace

            if event == "return":
                state = frame_state.get(frame)
                if state:
                    now = time.perf_counter()
                    elapsed = now - state["last_time"]

                    lineno = state["last_line"]
                    timings[lineno] = timings.get(lineno, 0) + elapsed

                    del frame_state[frame]

                return trace

            return trace

        # 🔑 Save previous tracer (IMPORTANT for nesting)
        old_trace = sys.gettrace()
        sys.settrace(trace)

        try:
            result = func(*args, **kwargs)
        finally:
            sys.settrace(old_trace)

        # 📊 Print report
        print(f"\n{Color.YELLOW}🔍 LinePulse Report for {func.__name__}:{Color.RESET}\n")

        for idx, line in enumerate(lines):
            lineno = start_line + idx
            elapsed = timings.get(lineno, 0)

            # color thresholds
            if elapsed > 0.3:
                color = Color.RED
            elif elapsed > 0.1:
                color = Color.YELLOW
            else:
                color = Color.GREEN

            print(f"{color}{lineno:4} | {elapsed:.6f}s | {line.rstrip()}{Color.RESET}")

        return result

    return wrapper