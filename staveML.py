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

##  getConfidence()
#   Returns a float 0 to 1 as a ratio of how many times
#   the entity appeared with final type.
#   Kat
def getConfidence(entity, documentEntities):
    return 0.0 

##  getAllQuotes(stave, persList) returns list[quote, name]
#   Jacob
#Given the writing style of the book, determining a name based on proximity to the quote is impossible. The functionality is taken out for now
def getAllQuotes(stave):
    '''
    (str) -> (list)
    Given a paragraph of text, finds the quotes, appends them to a list, and returns them
    Preconditions: Non quotation text must not be enclosed by quotations (This actually does happen for the first element of the sample list)
    '''

    stave = stave.replace('“','"')
    stave = stave.replace('”','"')
    quoteSplit = stave.split('"')
    quotes = []
    quoteStart = 1
    if stave[0] == '\"':
        quoteStart = 0


    for quote in range(quoteStart,len(quoteSplit),2):

        #speaker = "Unknown"
        #for person in persList:
            #if person in quoteSplit[quote+1]:
             #   speaker = person
            #elif person in quoteSplit[quote-1]:
            #    speaker = person

        quotes.append(quoteSplit[quote])

    return quotes

##  getSentiment(quote) returns signed float
#   Amy (Lin)

##  setElementTags(string, dictionary) returns string
#   Sina



############################################################
##  Main
#   Humam

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts

for entity in doc.ents:
    print(entity.text, entity.label_)


## end Main