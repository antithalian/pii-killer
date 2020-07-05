#!/usr/bin/python3

# pii-killer.py
# see README for functionality explanation

# imports
import praw
import json
import os

# load configuration
with open("secrets.json", "r") as secrets:
    secs = json.load(secrets)

# connect to reddit via praw
reddit = praw.Reddit(client_id=secs["client_id"], client_secret=secs["client_secret"], 
                    password=secs["password"], username=secs["username"], 
                    user_agent="PII killing script")