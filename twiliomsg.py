from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
from random import randint
import random 
import twilio.twiml
import urllib
import json
import unirest


app = Flask(__name__)

 
@app.route("/", methods=['GET', 'POST'])
def textline():
	if request.method == "GET":
		account_sid = "AC5e15f23d349b00ae2a044fdec01bed42"
		auth_token = "fb6567ba8daf7960c8fdbe0818b3ec5a"
		client = TwilioRestClient(account_sid, auth_token)

		user_num = request.values.get('From', None)
		user_request = request.values.get('Body', None)

		if user_request.lower() == 'quote':
			data = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous",
						headers={
							"X-Mashape-Key": "T7lnwsDWZWmshsvYwJU47QLGdxp1p1mEUqZjsnGnQYXpjmLkZP",
							"Content-Type": "application/x-www-form-urlencoded",
							"Accept": "application/json"
						})

			message = data.body['quote'] + '  -' + data.body['author']

		else:
			data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q="
					+ user_request 
					+ "&api_key=dc6zaTOxFJmzC&limit=10000").read())

			list_of_urls = []

			for dict_list in data['data']:
				if 'images' not in dict_list:
					message = 'You gave us some weird query... -_-'
					break
				print(dict_list['images']['fixed_height_small']['url'])
				list_of_urls.append(dict_list['images']['fixed_height_small']['url'])

			if list_of_urls == []:
				message = 'You gave us some weird query... -_-'
			else:
				rand_url = random.choice(list_of_urls)
				message = client.messages.create(to=user_num, from_="+13478366734", media_url=rand_url)

		resp = twilio.twiml.Response()
		resp.message(message)

		return str(resp)
     

if __name__ == "__main__":
    app.run(debug = True)
