import re


# -*- coding: utf-8 -*-
file = open('stave1.txt', 'r')
STAVE = file.read()
file.close()

#Talk to Jacob first
#905 920 5553 for Merge Conflicts
#Extract Each Paragraphs

PARAGRAPHS = STAVE.split('\n')

#Find speech in the parameter 'paragraph' return a array
#Richard


def findSpoken(paragraph):
    return {}


#Return a list of everytime word appears
#Returns the starting index of the word in a list


def getAllOccurance(word, section):

    list = []

    for i in re.finditer(word, section):
        list.append(i.start())

    return list



#Remove all punctuation 
#Jack

<<<<<<< HEAD
=======

>>>>>>> ee2d795837ebb7d17b9f36f78a8b222a6b2a62a6
def cleanStave():
    # define punctuation 
    punctuation = "'!()-[]\{\};:'\"\,<>./?@#$%^&*_~''"
    my_text = STAVE
    #to take input from the user
    #my_text = input("Enter stave1.txt")
    #remove punctuation from the stave
    no_punct = ""
    for char in my_text:
        if char not in punctuation:
            no_punct = no_punct + char
    #disply the unpunctuated text 
    print(no_punct)
        
    return no_puncts




print(getAllOccurance("Marley", STAVE))

