import spacy
nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("mnonkey")
word3 = nlp("banana")
word4 = nlp("software development")
word5 = nlp("natural language processing")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word5))  # returns a 0.6895.  The two are very similar. 

'''different result when run with en_corse_sm_model:
c:\Python Course\Task 38\semantic.py:13: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. 
This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
print(word4.similarity(word5))  # returns a 0.6895.  The two are very similar.
0.5984203684401248'''

tokens = nlp("cat apple monkey banana car wheel")  

# car and wheel return 0.5322, the words are un-alike but it's clear nlp knows they are closely related
# a different result of 0.3083 is given when using the en_core_web_sm model.  It's clearly not as 'intelligent'

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "why is my cat on the car"

sentances = ["where did my dog go,"
"Hello, there is my car",
"I\'ve lost my car in my car",
"i\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentances:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence +" - ", similarity)