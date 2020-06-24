author = "Anindita"

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag



def extractFeatures(file):
    entity={}
    word = nltk.word_tokenize(file)
    word = nltk.pos_tag(word)
    for item in word:
        if item[1]=='NNP':
            if item[0] in entity:
                entity[item[0]]+=1
            else:
                entity[item[0]]=1
    print(entity)




with open("001.txt") as file_read:
    contents = file_read.read()
    extractFeatures(contents)
    input()
