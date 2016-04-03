from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
from random import randint
import random 
import twilio.twiml
import urllib
import json


app = Flask(__name__)

 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    if request.method == "GET":
    	account_sid = "AC5e15f23d349b00ae2a044fdec01bed42"
    	auth_token = "fb6567ba8daf7960c8fdbe0818b3ec5a"
    	client = TwilioRestClient(account_sid, auth_token)

    	user_num = request.values.get('From', None)
        user_request = request.values.get('Body', None)

        data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=" 
        		+ user_request 
        		+ "&api_key=dc6zaTOxFJmzC&limit=10000").read())

        list_of_urls = []

        for thing in data['data']:
        	print(thing['images']['fixed_height']['url'])
        	list_of_urls.append(thing['images']['fixed_height']['url'])

        message = client.messages.create(to=user_num, from_="+13478366734", media_url=random.choice(list_of_urls))

        resp = twilio.twiml.Response()
        resp.message(message)

        return str(resp)
     

if __name__ == "__main__":
    app.run(debug = True)
