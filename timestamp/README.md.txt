# ⏰ Time Greeter in Python

This is a simple Python script that greets the user based on the current system time.

## 👋 Features

- Greets with:
  - "Good Morning" if the time is between 5 AM and 12 PM
  - "Good Afternoon" if the time is between 12 PM and 5 PM
  - "Good Evening" if the time is between 5 PM and 9 PM
  - "Good Night" for any other time
- Uses Python's built-in datetime module

## 🧠 How It Works

The script checks your local system time using:

```python
from datetime import datetime


Example output --

It's 8:35 AM
Good Morning! ☀️