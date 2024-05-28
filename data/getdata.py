import json
import random

def load_writing9():
    # Path to your JSON file
    filename = "./data/writing9.json"

    # Open the file in read mode
    with open(filename, "r") as f:
    # Load the data from the file
        ielts = json.load(f)

    return ielts

def load_simon():
    # Path to your JSON file
    filename = "./data/simon.json"

    # Open the file in read mode
    with open(filename, "r") as f:
    # Load the data from the file
        ielts = json.load(f)
        
    return ielts

def load_random(ielts):
    keys = list(ielts['data'].keys())
    return random.choice(keys)