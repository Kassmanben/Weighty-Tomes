import pickle

import nltk

with open('Book_Pickles/SampleDict.pkl', 'rb') as handle:
    bookshelf = pickle.load(handle)

print(bookshelf[2]["Description"])
print(nltk.word_tokenize(bookshelf[2]["Description"]))