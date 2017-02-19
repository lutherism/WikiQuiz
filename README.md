# WikiQuiz

![alt tag](http://i.imgur.com/Bx7l18S.png)


###To run:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python python/build.py
python python/server.py
```

###Potential Future Improvements:
Choosing more appropriate multiple-choice options, especially for numbers

_ie. if the answer is '1960s', show '1950s' as another option._

Ignoring the less text heavy parts of a Wikipedia page.

Creating more interesting grammar for the text chunker, which would lead to more interesting question types.

Some of the questions presented currently lack context about what the question is referring to. A further version of this project would attempt to interpret the context of the sentence in question and include that in the question.

_ie. references to 'they' or 'he' would be replaced by what those pronouns are actually referring to._

###Known limitations:
The Python script will not handle certain Wikipedia pages correctly ("Harry Potter" for example). Most likely due to how I'm iterating through the parsed token tree in create_questions in Article.py. Certain articles have disambiguations and I decided to leave handling these out of scope. For both of the above you'll see on the console that I'm just returning a 500 error. If working further on the project I'd fix these and create less overarching exception handling than the try/except in server.py
