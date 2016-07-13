from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
from random import randint
import random 
import twilio.twiml
import urllib
import json
import unirest
import settings # configurations file containing authorization keys, etc


app = Flask(__name__)

def get_quote():
	data = unirest.post(
		"https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous",
		headers= {
			"X-Mashape-Key": settings.mashape_key,
			"Content-Type": "application/x-www-form-urlencoded",
			"Accept": "application/json"
		}
	)
	response = data.body['quote'] + '  -' + data.body['author']
	return response


def get_joke():
	data = json.loads(urllib.urlopen("http://api.icndb.com/jokes/random/").read())
	response = data['value']['joke']
	return response


def get_url_list(data):
	url_list = []
	for dict_list in data:
		if 'images' not in dict_list:
			break
		# print(dict_list['images']['fixed_height_small']['url'])
		url_list.append(dict_list['images']['fixed_height_small']['url'])
	return url_list
	

def get_gif(user_num, user_request):
	data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q="
			+ user_request 
			+ "&api_key=" + settings.twilio_key + "&limit=10000").read())
	list_of_urls = get_url_list(data['data'])
	if list_of_urls == []:
		response = 'You gave us some weird query... -_-'
	else:
		rand_url = random.choice(list_of_urls)
		response = client.messages.create(to=user_num, from_=settings.number, media_url=rand_url)
		return response

 
@app.route("/", methods=['GET', 'POST'])
def textline():
	if request.method == "GET":
		client = TwilioRestClient(settings.account_sid, settings.auth_token)

		user_num = request.values.get('From', None)
		user_request = request.values.get('Body', None)

		if user_request.lower() == 'quote':
			message = get_quote()
		elif user_request.lower() == 'joke':
			message = get_joke()
		else:
			message = get_gif(user_num, user_request)

		resp = twilio.twiml.Response()
		resp.message(message)

		return str(resp)


if __name__ == "__main__":
    app.run(debug = True)
