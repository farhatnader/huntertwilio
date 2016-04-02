from twilio.rest import TwilioRestClient
import twilio.twiml
from random import randint
from flask import Flask, request
# Find these values at https://twilio.com/user/account

app = Flask(__name__)

def jokecreator ():
	myjokedictionary = ["whats hairy and red all over", 
						"the thundercats will live again", 
						"boogers are funny", 
						"farts make people laugh but they stink"]
	return myjokedictionary[randint(0,3)]


account_sid = "AC5e15f23d349b00ae2a044fdec01bed42"
auth_token  = "fb6567ba8daf7960c8fdbe0818b3ec5a"
client = TwilioRestClient(account_sid, auth_token)


@app.route("/", methods=['GET', 'POST'])
def main():
	# if request.method == 'GET': 
		message = client.messages.create(to="+17186400449", from_="+13478366734",
                                     body= jokecreator() )

		return message;
	

if __name__ == "__main__":
    app.run(debug=True)