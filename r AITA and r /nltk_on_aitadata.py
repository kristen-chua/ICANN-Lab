import nltk
import csv
from csv import reader
#nltk.download() #opens nltk downloader, downloaded 93mtaggers/averaged_perceptron_tagger/averaged_perceptron_tagger.pickl


tokens=nltk.word_tokenize("AITA for telling my future SIL that I won’t be attending her childfree wedding causing a lot of my other family members to drop out as well")

#print("Tokens: ", tokens)
print("Parts of Speech: ", nltk.pos_tag(tokens)) #prints out between [ ], so it is a list



## data to be written row-wise in csv fil
pos_data = nltk.pos_tag(tokens)
#opening the csv file in 'a+' mode
file=open('test.csv','a+',newline = '')


# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(pos_data)
