import numpy as np
import nltk
import string
import random

f=open('E:/PY/Chatbot_project.py/chat.txt','r',errors = 'ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower() 
nltk.download('punkt') 
nltk.download('wordnet') 
sent_tokens = nltk.sent_tokenize(raw_doc) 
word_tokens = nltk.word_tokenize(raw_doc) 
sent_tokens[:2]
word_tokens[:2]

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey")
GREET_RESPONSES = ["hi!!!", "hey bro!!!", "paheli fursat me nikalll", "hi there", "kya hello hello", "Wow!!!You are talking to me,,Great!!!"]
def greet(sentence):
 
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def response(user_response):
  robo1_response=''
  TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
  tfidf = TfidfVec.fit_transform(sent_tokens)
  vals = cosine_similarity(tfidf[-1], tfidf)
  idx=vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if(req_tfidf==0):
    robo1_response=robo1_response+"Bro!!!! Please write meaningful,,,OK?"
    return robo1_response
  else:
    robo1_response = robo1_response+sent_tokens[idx]
    return robo1_response

flag=True
print("My Name is BOT!!!! To Kese hai AAP LOG!!!!! Let's have a conversation! Also, if you don't want to talk, then go yarrr!!!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("BOT: You are welcome..")
        else:
            if(greet(user_response)!=None):
                print("BOT: "+greet(user_response))
            else:
                sent_tokens.append(user_response)
                word_tokens=word_tokens+nltk.word_tokenize(user_response)
                final_words=list(set(word_tokens))
                print("BOT: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("BOT: Goodbye! Take care")