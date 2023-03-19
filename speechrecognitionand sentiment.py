import speech_recognition as sr

# create a recognizer instance
r = sr.Recognizer()
 
# use the default microphone as the audio source
with sr.Microphone() as source: 
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    print( r.recognize_google(audio))
    sentence=r.recognize_google(audio)
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
from textblob import TextBlob

def get_sentiment(sentence):
    
    blob = TextBlob(sentence)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'
print(get_sentiment(sentence))
