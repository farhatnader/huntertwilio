from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
from random import randint 

import twilio.twiml
 
app = Flask(__name__)
 
def jokecreator ():
    myjokedictionary = ["whats hairy and red all over", "http://www.vitaminbeyonce.com/", "http://www.randomgoat.com/", "farts make people laugh but they stink", 
                        "if God was a bird, he'd be a bird"]
    return myjokedictionary[randint(0,4)]

# Try adding your own number to this list!
callers = {
    "+17184165926": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+17184165926": "Chris"
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
    if request.method=="GET":
        from_number = request.values.get('From', None)
        if from_number in callers:
            message = jokecreator();
        else:
            message = "Monkey, thanks for the message!"

        resp = twilio.twiml.Response()
        resp.message(message)

        return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
