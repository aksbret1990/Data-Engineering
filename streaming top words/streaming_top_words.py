#importing modules/libraries

import threading
import time
from csv import reader
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter



#this function is to insert new lines before you see the next output
def cls():
    print('\n' * 100)

#this function simualtes streaming data. For every 1 second, a stream of data i.e. one row of text column is received
def get_streaming_data():
    with open("file.csv") as file:
        global all_words
        csv_reader = reader(file)
        next(csv_reader, None)  # skip the headers
        exclude = set(string.punctuation) #get all punctuations
        stop_words = set(stopwords.words('english')) #get all stop words
        for row in csv_reader:
            text = row[1]
            text_without_punctutation = ''.join(ch for ch in text if ch not in exclude)
            word_tokens = word_tokenize(text_without_punctutation)
            words = [w for w in word_tokens if w not in stop_words and not w.isdigit()]
            words.reverse() 
            all_words = words + all_words
            time.sleep(1)

#this function returns the top words and their respective counts from the list of latest 1000 streamed words        
def get_count():
    counts = Counter(all_words[:1000])
    return counts
    #return all_words


all_words = []
thread = threading.Thread(target=get_streaming_data, args=())
thread.start()    
yesno = 'y'
while yesno == 'y':
    yesno = input('Do you want to know top words and their count from the last 1000 words? If yes press \'y\' else any other key: ')  
    cls()
    print(get_count())
