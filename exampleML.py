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

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

## getConfidence()
# Returns a float 0 to 1 as a ratio of how many times
# the entity appeared with final type.
def getConfidence(entity, documentEntities):
    return 0.0 

## getAllQuotes(stave) returns list[quote, name]
# 

## getSentiment(quote) returns signed float
#

## setElementTags(string, dictionary) returns string
#



############################################################
## Main

## end Main