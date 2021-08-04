import spacy #for dependency trees
nlp = en_core_web_sm.load()

#https://neptune.ai/blog/exploratory-data-analysis-natural-language-processing-tools
import nltk
import csv
from nltk.tokenize import word_tokenize
from csv import reader
#nltk.download() #opens nltk downloader, downloaded 93mtaggers/averaged_perceptron_tagger/averaged_perceptron_tagger.pickl


### Get each unique word in a csv file tokenized
### https://stackoverflow.com/questions/58046661/get-each-unique-word-in-a-csv-file-tokenized
words = []

def get_data():
    with open("title parsed_relationships only.csv", "r") as records:
        for record in csv.reader(records):
            yield record

data = get_data()
next(data)  # skip header

for row in data:
    for sent in row:
        for word in word_tokenize(sent):
            #if word not in words: # this means we get the full sentence, not just unique words
            words.append(word)
print(words)


### Tokenization and Parts of Speech(POS) Tagging in Python’s NLTK library
### https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b

#tokens=nltk.word_tokenize("AITA for telling my future SIL that I won’t be attending her childfree wedding causing a lot of my other family members to drop out as well")
#
#print("Tokens: ", tokens)
#print("Parts of Speech: ", nltk.pos_tag(tokens)) #prints out between [ ], so it is a list
#
#
#
## data to be written row-wise in csv file
pos_data = nltk.pos_tag(words)

### Writing data from a Python List to CSV row-wise
### https://www.geeksforgeeks.org/writing-data-from-a-python-list-to-csv-row-wise/
#opening the csv file in 'a+' mode
file=open('POS_title parsed_relationships only.csv','a+',newline = '')
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(pos_data)
