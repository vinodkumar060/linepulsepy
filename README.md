# 🔥 linepulsepy

[![PyPI version](https://img.shields.io/pypi/v/linepulsepy?color=blue)](https://pypi.org/project/linepulsepy/) 
[![License](https://img.shields.io/badge/license-Proprietary-red)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://www.python.org/)
[![Downloads](https://img.shields.io/pypi/dt/linepulsepy)](https://pypi.org/project/linepulsepy/)

**linepulsepy** is a lightweight Python package that helps developers instantly identify slow lines of code using a simple decorator. Perfect for debugging, optimization, and performance tuning.

---

## 🌟 Features

- Line-by-line execution time tracking  
- Color-coded output for fast, medium, and slow lines  
- Simple decorator: just add `@profile_lines`  
- Works with any Python function  
- No external dependencies  

---

## 📸 Screenshots / Example Output

```text
🔍 LinePulse Report for sample:

   10 | 0.000001s | x = 0
   11 | 0.500234s | for i in range(5):
   12 | 0.000002s |     x += i
