# app.py
import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def notify():
    print("Sending alert...")
