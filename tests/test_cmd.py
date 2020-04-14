import questions
import requests
import os
from os import getenv
import ctx
# from weather import Weather, Unit
from datetime import datetime
import pytz
import random # pip install random2
import site
import sys
import config
import numpy as np


def chat():
	print("Hi there, I'm AI-bot!")
	while True:
		inp = input("You: ")
		if inp == "quit":
			break
		elif "!" in str(inp):
			print("Add your answer to the bot script")
			inp2 = input("You: ")
		elif "?" in str(inp):
			print("Add your question to the bot script")
			inp2 = input("You: ")
		else:
			print("I don't know what to say, but you can teach me.")
			print("'!' is for adding an answer to the previous question.")
			print("'?' is for adding a question to the previous answer.")

chat()
