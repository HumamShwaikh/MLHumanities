# pip install spacy
# python -m spacy download en_core_web_sm

import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
file = open('stave1.txt',mode='r',encoding='UTF8')
text = file.read()
doc = nlp(text)
file.close()

#make list of tuples from doc.ents and their attributes
lst = []
def makeTupleList():
    for entity in doc.ents:
        lst.append((entity.text, entity.label_))
    return lst
lst = makeTupleList()


#define dictionary of tuple entities where keys are names
def convert(entityTuples, entityDictionary):
    for x, y in entityTuples:
        entityDictionary.setdefault(x, []).append(y)
    return entityDictionary

entityDict = {}
entityDict = convert(lst, entityDict)

##  getConfidence()
#   Returns a float 0 to 1 as a ratio of how many times
#   the entity appeared with final type.
#   Kat
def getConfidence(entity, documentEntities):
    return 0.0 

##  getAllQuotes(stave) returns list[quote, name]
#   Jacob

##  getSentiment(quote) returns signed float
#   Amy (Lin)

##  setElementTags(string, dictionary) returns string
#   Sina



############################################################
##  Main
#   Humam

# Analyze syntax
#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
#print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
#for entity in doc.ents:
   # print(entity.text, entity.label_)

#print(entityDict)
print(entityDict)
## end Main