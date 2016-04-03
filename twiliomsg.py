from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
from random import randint
import random 
import twilio.twiml
import urllib
import json


app = Flask(__name__)


def jokecreator ():
    myjokedictionary = ["whats hairy and red all over", 
    					"http://www.vitaminbeyonce.com/", 
    					"http://www.randomgoat.com/", 
    					"farts make people laugh but they stink"]
    return myjokedictionary[randint(0,3)]

 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    if request.method == "GET":
       user_request = request.values.get('Body', None)

       data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q="
               + user_request
               + "&api_key=dc6zaTOxFJmzC&limit=5").read())
       list_of_urls = []
       for thing in data['data']:
           print(thing['images']['fixed_height']['url'])
           list_of_urls.append(thing['images']['fixed_height']['url'])

       message = random.choice(list_of_urls)
       resp = twilio.twiml.Response()
       resp.message(message)
       return str(resp)


if __name__ == "__main__":
    app.run(debug = True)
