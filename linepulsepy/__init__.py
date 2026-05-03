"""
linepulsepy - Line-by-line Python performance profiler

A lightweight developer tool that helps identify slow lines of code
inside functions using a simple decorator.

Features:
- Line-by-line execution time tracking
- Source code display with timings
- Color-coded performance output
- No external dependencies

Example:
    from linepulsepy import profile_lines

    @profile_lines
    def test():
        x = 0
        for i in range(5):
            x += i
        return x

    test()
"""

from .profiler import profile_lines

__version__ = "0.1.2"