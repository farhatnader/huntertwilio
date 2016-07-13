#TwiliPhy

```pip install Flask```
```pip install twilio```

Run: ```python twiliomsg.py```

While it is running on a server, it works by a user sending a text message to the number:
```13478366734```

The user may prompt anything. 
If it is "quote", the user will receive a randomly generated quote from a famous person.
If it is "joke", the user will receive a randomly generated joke.
If it is someting else, so long as it exists, the user will be sent a random GIF of said thing.