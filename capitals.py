capitals_dict = {
    "British Columbia": "Victoria",
    "Alberta": "Edmonton",
    "Saskatchewan": "Regina",
    "Manitoba": "Winnipeg",
    "Ontario": "Toronto",
    "Quebec": "Quebec",
    "New Brunswick": "Fredericton",
    "Nova Scotia": "Halifax",
    "Prince Edward Island": "Charlottetown",
    "Newfoundland & Labrador": "St. John's",
    "Yukon": "Whitehorse",
    "Northwest Territories": "Yellowknife",
    "Nunavut": "Iqaluit",
    }

import random

provinces = capitals_dict.keys()
for i in range(5):
    province = random.choice(provinces)
    capital = capitals_dict[province]
    capital_guess = raw_input("What is the capital of " + province + "? ")

    if capital_guess == capital:
        print "Correct! Nice job."
    else:
        print "Incorrect. The capital of " + province + " is " + capital + "."

print "All done"
