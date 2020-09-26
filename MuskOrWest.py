### File Name: MustOrWest.py
# Description: [Change++ Application 2020] A game which tests the user on their ability to
#              differentiate tweets between two individuals: Elon Musk and Kanye West.
# Author: Seok Hee Hong

### Import Statements
import tweepy
import http.client
import mimetypes
import random
import json

### Variables
win_count = 0
lose_count = 0
random_num = random.randint(0, 1)
index = 0
continue_game = 1

### Fetching data from @elonmusk
conn = http.client.HTTPSConnection("api.twitter.com")
payload = ''
headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMwxIAEAAAAATcq8qJdQEC9hcFyIzQmNcOmHBIc%3DLd9c7FwXsP7SWLcI0DDizrXtjMSRx61HDHtV8niYC3xXkHgDsW',
    'Cookie': 'personalization_id="v1_QG/7J7mFRMIGm3XGfxGYGw=="; guest_id=v1%3A160108074660260180'
}
conn.request("GET", "/1.1/statuses/user_timeline.json?screen_name=elonmusk&count=3200&exclude_replies=true&include_rts=false", payload, headers)
res = conn.getresponse()
musk_data = res.read()
# print(musk_data.decode("utf-8"))

### Fetching data from @kanyewest
conn = http.client.HTTPSConnection("api.twitter.com")
payload = ''
headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMwxIAEAAAAATcq8qJdQEC9hcFyIzQmNcOmHBIc%3DLd9c7FwXsP7SWLcI0DDizrXtjMSRx61HDHtV8niYC3xXkHgDsW',
    'Cookie': 'personalization_id="v1_QG/7J7mFRMIGm3XGfxGYGw=="; guest_id=v1%3A160108074660260180'
}
conn.request("GET", "/1.1/statuses/user_timeline.json?screen_name=kanyewest&count=3200&exclude_replies=true&include_rts=false", payload, headers)
res = conn.getresponse()
west_data = res.read()
# print(west_data.decode("utf-8"))


### Game Loop
# Repeats the game as long as the user answers that they want to.
while continue_game:
    # Generates a random quote and displays it.
    random_num = random.randint(0, 1)

    if random_num:
        # print(musk_data[index]['text'])
        answer = "MUSK"
    else:
        # print(west_data[index]['text'])
        answer = "WEST"


    # Asks the user who they think tweeted the quote.
    input_who = input("Who Tweeted this? Musk or West?")

    if input_who.upper() == answer:
        win_count += 1
        print("Correct!")
    else:
        lose_count += 1
        print("Nope!")

    # The index (the index of the datasets) increases (for the next found, if played).
    index += 1

    # Print the game statistics.
    print("Win: " , win_count, " | Lose: ", lose_count)

    # Asks if the user wants to continue the game.
    continue_game_input = input("Do you want to continue? print 'Y' or 'N'")
    if continue_game_input.upper() == "Y":
        print("Next question: ")
        continue_game = 1
    else:
        print("Thanks for playing!")
        continue_game = 0