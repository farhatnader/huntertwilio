from twilio.rest import TwilioRestClient
from random import randint 
# Find these values at https://twilio.com/user/account

def jokecreator ():
	myjokedictionary = ["whats hairy and red all over", "the thundercats will live again", "boogers are funny", "farts make people laugh but they stink", 
						"if God was a bird, he'd be a bird"]
	return myjokedictionary[randint(0,4)]


account_sid = "AC5e15f23d349b00ae2a044fdec01bed42"
auth_token  = "fb6567ba8daf7960c8fdbe0818b3ec5a"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+17186400449", from_="+13478366734",
                                     body= jokecreator() )