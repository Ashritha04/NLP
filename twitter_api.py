import tweepy as tw
import configparser
import pandas as pd


import string
from collections import Counter

import matplotlib.pyplot as plt

import re


import nltk
#nltk.download('stopwords')  #this is to download the stop words , not required to run all time
from nltk.corpus import stopwords



import warnings
warnings.filterwarnings("ignore")

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

 
# authentication
auth = tw.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth,wait_on_rate_limit=True)




# user tweets
user = 'KTRTRS'
limit=100

tweets = tw.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)



def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : stringr]=
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())



# create DataFrame
#columns = ['User', 'Tweet']
#data = []

#for tweet in tweets:
 #   data.append([tweet.user.screen_name, remove_url(tweet.full_text)])

#df = pd.DataFrame(data, columns=columns)

#print(df)

#csv_data = df.to_csv('./Data/myfile1.csv')  

list1=[]

for tweet in tweets:
    x=remove_url(tweet.full_text)
    #y=tweet.full_text
    list1.append(x)


text =" "

length = len(list1)
#for i in list1:
    #print(i,end='\n')
    #print("\n")

text = " ".join(list1)
print(text)

lower_converted = text.lower()   #converting to lower case
#print(string.punctuation)  #just to check what are the punctuations in python
cleaned_text = lower_converted.translate(str.maketrans('','',string.punctuation)) 
tokenized_words = cleaned_text.split()
#print(tokenized_words)

stop_words=stopwords.words('english')
#print(stop_words)

final_list =[]
dummy=[]
for word in tokenized_words:
    if(word not in stop_words):
        final_list.append(word)
    else:
        dummy.append(word)
#print(dummy)

#print(final_list)

emotion_list =[]
with open('emotions.txt','r') as file:
    for line in file:
        #print(line)
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        #print(clear_line)
        word,emotion = clear_line.split(':')
       # print("word : "+word +"  "+" emotion : " +emotion)\

        if word in final_list:
            emotion_list.append(emotion)
#print(emotion_list)

w=Counter(emotion_list)
#print(w)

plt.bar(w.keys(),w.values())
plt.xticks(rotation=90)
#plt.savefig('graph1.png')
plt.show()
