# pip install spacy
# python -m spacy download en_core_web_sm

import spacy
import operator
import example

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
file = open('stave1.txt',mode='r',encoding='UTF8')
text = file.read()
doc = nlp(text)
file.close()

#make list of tuples from doc.ents, 
# type of each tuple is (string entity name,string entity label)
lst = []
def makeTupleList():
    for entity in doc.ents:
        lst.append((entity.text, entity.label_))
    return lst
lst = makeTupleList()


# define dictionary of tuple entities where keys are nouns, 
# values per key are lists of noun's associations to text
def convert(entityTuples, entityDictionary):
    for x, y in entityTuples:
        entityDictionary.setdefault(x, []).append(y)
    return entityDictionary

entityDict = {}
entityDict = convert(lst, entityDict)

##  getConfidence()
#   Returns a float 0 to 1 as a percentage of how many times
#   the entity appeared with final type.
#   Kat
def getConfidence(entity, documentEntities):

    #create list of labels for passed entity
    entityNounList = documentEntities[entity]
    #create dictionary with key as labels and values as number of occurances per label for passed entity
    counterDict = {i:entityNounList.count(i) for i in entityNounList}
    #find the entity label with the highest occurance number
    maxKey = max(counterDict.items(), key=operator.itemgetter(1))[0]
    #total number of times labels were attributed to entity
    totalMentionLabels = sum(counterDict.values())
    maxEntOccur = counterDict.get(maxKey)
    
    return (maxEntOccur/totalMentionLabels)

##  getAllQuotes(stave) returns list[quote, name]
#   Jacob

##  getSentiment(quote) returns signed float
#   Amy (Lin)




##  When given a list of names, it goes through each name and adds a tag before and after the name.
##  In this case, it was designed for <persName>
#   Sina

def setElementTag(String, Dictionary, section):

    for index in Dictionary:
        List=example.getAllOccurance(index, section)

        for i in range(0,len(List),2):
            output=section[:List[i]]+"<"+String+">"+index
            output2="<"+"/"+String+">"+section[List[i+1]:]
            output3=output+output2
            section=output3
            List=example.getAllOccurance(index,section)
    return section

###########################################################
# Program to find most frequent  
# element in a list 
def most_frequent(List): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(List): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm) 

############################################################
##  Main
#   Humam

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
   print(entity.text, entity.label_)

#Show Entity Dictionary
print("\nThe following is the dictionary of entities:\n")
print(entityDict)

#Add confidence to all keys
for key in entityDict:
    conf = getConfidence(key,entityDict)
    entityDict[key] = [most_frequent(entityDict[key]), conf]
    print(key + " " + str(entityDict[key]))


## end Main