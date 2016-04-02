# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC5e15f23d349b00ae2a044fdec01bed42"
auth_token  = "fb6567ba8daf7960c8fdbe0818b3ec5a"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+13476979332", from_="+13478366734",
                                     body="RANDOM JOKE FUNCTION")