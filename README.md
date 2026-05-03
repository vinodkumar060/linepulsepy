# 🔥 linepulsepy

[![PyPI version](https://img.shields.io/pypi/v/linepulsepy?color=blue)](https://pypi.org/project/linepulsepy/) 
[![License](https://img.shields.io/badge/license-Proprietary-red)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://www.python.org/)
[![Downloads](https://img.shields.io/pypi/dd/linepulsepy)](https://pypi.org/project/linepulsepy/)

**linepulsepy** is a lightweight Python package that helps developers instantly identify slow lines of code using a simple decorator. Perfect for debugging, optimization, and performance tuning.

---

## 🌟 Features

- Line-by-line execution time tracking  
- Color-coded output for fast, medium, and slow lines  
- Simple decorator: just add `@profile_lines`  
- Works with any Python function  
- No external dependencies  

---

## 📦 Installation

```bash
pip install linepulsepy
```
---

## 📸 Screenshots / Example Output

---
```text
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
```

<img width="820" height="144" alt="Screenshot 2026-05-01 at 10 43 49 PM" src="https://github.com/user-attachments/assets/3fbc5c81-e128-4a0a-98df-c8ca0144d6f8" />



