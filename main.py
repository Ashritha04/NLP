#cleaning text steps
#1)Create a text file and take text from it
#2)convert the letter into lower case 
#3)remove punctuations.

import string
from collections import Counter # for counting the emotions repetation from the list.
import matplotlib.pyplot as plt
#encoding(it is just the way of writing the text on internet)
text = open('read.txt',encoding='utf-8').read() #opening and reading the file
lower_case = text.lower() #converting the text in read.txt file to lowercase
#print(lower_case)

#print(string.punctuation) # to check the predefined punctuations.


#str1: specifies the list of characters that needs to be replaced
#str2: specifies the list of characters with which the characters needs to be replaced
#str3: specifies the list of characters that needs to be replaced
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))#translate removes the punctuations

#tokenisation- process of splitting the words
#tokenisation is required becoz NLP is analysis of words but not sentences

tokenized_words = cleaned_text.split()
#print(tokenized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words=[]
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

#print(final_words)

# ctrl+alt+n for formatting 
# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

emotions_list=[]
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotions_list.append(emotion)

print(emotions_list)
w = Counter(emotions_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()