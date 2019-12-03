import re


# -*- coding: utf-8 -*-
file = open('stave1.txt', mode='r', encoding='UTF8')
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
        list.append(i.end())
    return list



#Remove all punctuation 
#Jack


def cleanStave():
    newStave = STAVE
    
    return newStave




print(getAllOccurance("Marley", STAVE))

