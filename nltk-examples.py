import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

## Using NLTK to tokenize a sentence and get the POS ##

sagan = "We live in a society exquisitely dependent on science and technology, in which hardly anyone knows anything about science and technology."

# Tokenize the sentence
tokens = word_tokenize(sagan);

# Used to figure out the Part of Speech
# See http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html for meanings of POS tags
pos = nltk.pos_tag(tokens)
print("\nTokenized sentence with POS:\n");
print(pos);


## Using NLTK to get the definition of a word ##
print("\nDefinition of Ireland:\n");
syn = wordnet.synsets("ireland")
print(syn[0].definition())


## Using NLTK to get get example usage of a word ##
print("\nExample usage of work 'manner':\n");
syn = wordnet.synsets("manner")
print(syn[0].examples())


## Getting Hypernyms and Hyponyms  ##
# Hypernym is the root of the word, e.g. colour is the hypernym of red. Hyponyms are similar words, like the colors blue, green etc.
print("\nHyperyms and Hyponyms of word 'country':\n");
syn = wordnet.synsets("country")[0]
print(syn.hypernyms())
print(syn.hyponyms())


## Get the opposite (antonym) of a word ##
print("\nOpposite of word 'good':\n");
syn = wordnet.synsets("good")
for s in syn:
    for l in s.lemmas():
        if (l.antonyms()):
            print(l.antonyms())