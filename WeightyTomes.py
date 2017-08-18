import pickle
import re
import string
import sys


class Book:
    def __init__(self, title, author, genre, description):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description

    def __str__(self):
        return str(self.title) + "\n" + str(self.author) + "\n" + str(self.description) + "\n" + str(self.genre)

    def __hash__(self):
        return hash((self.title, self.author, self.genre, self.description))

    def __eq__(self, other):
        return (self.title, self.author, self.genre, self.description) == (
            other.title, other.author, other.genre, other.description)

    def __ne__(self, other):
        return not (self == other)


class ImproperFrac:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def __eq__(self, other):
        return self.toint() == other.toint()

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash((self.num, self.den))

    def toint(self):
        if self.num != 0 and self.den != 0:
            decint = (int(self.num)) / (int(self.den))
        if self.num != 0 and self.den == 0:
            print("CANNOT DIVIDE BY ZERO")
            return
        if self.num == 0 and self.den == 0:
            print("RELATED TO ONLY ITSELF")
            return 1
        return decint

    def up_numden(self):
        self.num += 1
        self.den += 1

    def up_den(self):
        self.den += 1

    def up_num(self):
        self.num += 1


from nltk.tokenize import word_tokenize

with open('Book_Pickles/SampleDict.pkl', 'rb') as handle:
    bookDict = pickle.load(handle)
with open('Book_Pickles/Bookshelf.pkl', 'rb') as handle:
    bookshelf = pickle.load(handle)
with open('Book_Pickles/WordList.pkl', 'rb') as handle:
    wordset = pickle.load(handle)
with open('Text_Pickles/Dictionary.pkl', 'rb') as handle:
    dictionary = pickle.load(handle)
with open('Book_Pickles/NameDict.pkl', 'rb') as handle:
    namedictionary = pickle.load(handle)
with open('Text_Pickles/AcceptableHyphens.pkl', 'rb') as handle:
    acceptablehyphens = pickle.load(handle)
with open('Text_Pickles/stopwords.pkl', 'rb') as handle:
    stopset = pickle.load(handle)
with open('Text_Pickles/UnacceptableHyphens.pkl', 'rb') as handle:
    unacceptablehyphens = pickle.load(handle)
with open('Book_Pickles/AuthorArray.pkl', 'rb') as handle:
    authors_related_to = pickle.load(handle)
with open('Book_Pickles/GenreArray.pkl', 'rb') as handle:
    genres_related_to = pickle.load(handle)
with open('Book_Pickles/TitleArray.pkl', 'rb') as handle:
    titles_related_to = pickle.load(handle)
with open('Book_Pickles/WordRelations.pkl', 'rb') as handle:
    words_related_to = pickle.load(handle)


def close_the_pickle_jar(cbookshelf, cwordlist, authorlist, genrelist, titlelist, wordrelations, cbookDict,
                         cnamedictionary, cstopset, cacceptablehyphens,
                         cunacceptablehyphens, cdictionary):
    with open('Book_Pickles/Bookshelf.pkl', 'wb') as rehandle5:
        pickle.dump(cbookshelf, rehandle5, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Book_Pickles/WordList.pkl', 'wb') as rehandle6:
        pickle.dump(cwordlist, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Book_Pickles/AuthorArray.pkl', 'wb') as rehandle6:
        pickle.dump(authorlist, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Book_Pickles/GenreArray.pkl', 'wb') as rehandle6:
        pickle.dump(genrelist, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Book_Pickles/TitleArray.pkl', 'wb') as rehandle6:
        pickle.dump(titlelist, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Book_Pickles/WordRelations.pkl', 'wb') as rehandle6:
        pickle.dump(wordrelations, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Book_Pickles/SampleDict.pkl', 'wb') as rehandle6:
        pickle.dump(cbookDict, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Book_Pickles/NameDict.pkl', 'wb') as rehandle6:
        pickle.dump(cnamedictionary, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Text_Pickles/stopwords.pkl', 'wb') as rehandle6:
        pickle.dump(cstopset, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Text_Pickles/AcceptableHyphens.pkl', 'wb') as rehandle6:
        pickle.dump(cacceptablehyphens, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Text_Pickles/UnacceptableHyphens.pkl', 'wb') as rehandle6:
        pickle.dump(cunacceptablehyphens, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
    with open('Text_Pickles/Dictionary.pkl', 'wb') as rehandle6:
        pickle.dump(cdictionary, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)


def dictionary_questions(wordd):
    if wordd.__contains__("'s"):
        wordd = wordd.replace("'s", "")
        dictionary_questions(wordd)
    if wordd.__contains__("’s"):
        wordd = wordd.replace("’s", "")
        dictionary_questions(wordd)
    if wordd in namedictionary and wordd.lower() not in dictionary:
        return wordd
    if wordd.lower() in dictionary:
        return wordd.lower()
    if wordd not in acceptablehyphens:
        if wordd.__contains__("-"):
            wordd = wordd.split("-")
            for element in wordd:
                dictionary_questions(element)
        if wordd.__contains__("—"):
            wordd = wordd.split("—")
            for element in wordd:
                dictionary_questions(element)
        return "the"
    for punct in set(string.punctuation):
        if punct == "-" or punct == "—":
            continue
        abbreivname = re.search("([A-Z])\.", wordd)
        if abbreivname:
            continue
        if wordd.__contains__(str(punct)):
            wordd = wordd.replace(str(punct), "")
            dictionary_questions(wordd)
    if wordd.isdecimal():
        return "the"
    if wordd.islower():
        g = input(str(wordd) + " wl?")
        if g != "n":
            dictionary.add(wordd)
            return wordd
    if wordd.istitle():
        g = input(str(wordd) + " name?")
        if g != "n":
            namedictionary.add(wordd)
            return wordd
    f = input(str(wordd))
    if f == "wc":
        dictionary.add(wordd)
        return wordd
    if f == "wl":
        dictionary.add(wordd.lower())
        return wordd.lower()
    if f == "n":
        namedictionary.add(wordd.capitalize())
        return wordd.capitalize()
    if f == "b":
        dictionary.add(wordd.lower())
        namedictionary.add(wordd)
        g = input("context?")
        if g == "w":
            return wordd.lower()
        if g == "n":
            return wordd
        return "the"
    if f == "h" and wordd.__contains__("-"):
        unacceptablehyphens.add(wordd)
        wordd = wordd.split("-")
        for element in wordd:
            dictionary_questions(element)
        return "the"
    if f == "h" and wordd.__contains__("—"):
        unacceptablehyphens.add(wordd)
        wordd = wordd.split("—")
        for element in wordd:
            dictionary_questions(element)
        return "the"
    if f == "p":
        stopset.add(wordd)
        return "the"
    if f == "x":
        g = input("char to remove?")
        if wordd.__contains__(str(g)):
            wordd = wordd.replace(str(g), "")
            dictionary_questions(wordd)
        return "the"


# noinspection PyTypeChecker
def reevaluate():
    newbookshelf = {}
    newwordset = set()
    for i in range(1, len(bookDict)):
        text = word_tokenize(bookDict[i]['Description'])
        # text = bookDict[i]['Description']
        text2 = []
        for newword in text:
            if type(newword) is str and newword.lower() not in stopset:
                if newword in namedictionary and newword.lower() not in dictionary:
                    text2.append(newword)
                    continue
                if newword.lower() in dictionary:
                    text2.append(newword.lower())
                    continue
                if str(newword.lower()) not in dictionary and str(newword) not in namedictionary:
                    text2.append(dictionary_questions(newword))
                    continue
        for element in text2:
            if type(element) == str:
                newwordset.add(element)
        filter(None, text2)
        bookDict[i]['Description'] = text2
        text = word_tokenize(bookDict[i]['Title'])
        # text = bookDict[i]['Title']
        text2 = []
        for newword in text:
            if type(newword) is str and newword.lower() not in stopset:
                if newword in namedictionary and newword.lower() not in dictionary:
                    text2.append(newword)
                    continue
                if newword.lower() in dictionary:
                    text2.append(newword.lower())
                    continue
                if str(newword.lower()) not in dictionary and str(newword) not in namedictionary:
                    text2.append(dictionary_questions(newword))
                    continue
        for element in text2:
            if type(element) == str:
                newwordset.add(element)
    for i in range(1, len(bookDict)):
        book = Book(bookDict[i]['Title'], bookDict[i]['Author'], bookDict[i]['Genre'], bookDict[i]['Description'])
        newbookshelf[book.title] = [book.title.strip(), book.author.strip(), book.genre, book.description]
    close_the_pickle_jar(newbookshelf, newwordset, authors_related_to, genres_related_to, titles_related_to,
                         words_related_to, bookDict, namedictionary, stopset, acceptablehyphens,
                         unacceptablehyphens, dictionary)


# Used to update book tables, wordset, dictionaries and
#
# reevaluate()
# sys.exit(0)

for key, book in bookshelf.items():
    print(sorted(book[3]))
for element in wordset:
    words_related_to[element.strip()] = [[element.strip()], (element.strip(), ImproperFrac(0, 0))]
for key, book in bookshelf.items():
    titles_related_to[book[0]] = [[book[0]], (book[0], ImproperFrac(0, 0))]
    authors_related_to[book[1]] = [[book[1]], (book[1], ImproperFrac(0, 0))]
    if type(book[2]) is tuple:
        for i in range(0, len(book[2])):
            genres_related_to[book[2][i].strip()] = [[book[2][i].strip()], (book[2][i].strip(), ImproperFrac(0, 0))]
    else:
        genres_related_to[book[2].strip()] = [[book[2].strip()], (book[2].strip(), ImproperFrac(0, 0))]
for key, book in bookshelf.items():
    if type(book[2]) is tuple:
        for i in range(0, len(book[2])):
            for j in range(0, len(book[2])):
                if book[2][j] not in genres_related_to[book[2][i].strip()][0]:
                    genres_related_to[book[2][i].strip()].append((book[2][j].strip(), ImproperFrac(0, 0)))
                    genres_related_to[book[2][i].strip()][0].append(book[2][j].strip())

# print(words_related_to)
# print(titles_related_to)
# print(authors_related_to)
# print(genres_related_to)
for counter in range(0, 10):
    for key, book in bookshelf.items():
        for key2, book2 in bookshelf.items():
            if (book[1] == book2[1] and book[0] != book2[0]) and book2[0] not in \
                    titles_related_to[book[0]][0]:
                titles_related_to[book[0]].append((book2[0], ImproperFrac(0, 0)))
                titles_related_to[book[0]][0].append(book2[0])
                if type(book[2]) is tuple:
                    for genre in book[2]:
                        if type(book2[2]) is tuple:
                            for genre2 in book2[2]:
                                if genre2 not in genres_related_to[genre.strip()][0]:
                                    genres_related_to[genre.strip()].append((genre2.strip(), ImproperFrac(0, 0)))
                                    genres_related_to[genre.strip()][0].append(genre2.strip())
                        else:
                            if book2[2] not in genres_related_to[genre.strip()][0]:
                                genres_related_to[genre.strip()].append((book2[2].strip(), ImproperFrac(0, 0)))
                                genres_related_to[genre.strip()][0].append(book2[2].strip())
                else:
                    if type(book2[2]) is tuple:
                        for genre2 in book2[2]:
                            if genre2 not in genres_related_to[book[2].strip()][0]:
                                genres_related_to[book[2].strip()].append((genre2.strip(), ImproperFrac(0, 0)))
                                genres_related_to[book[2].strip()][0].append(genre2.strip())
                    else:
                        if book2[2] not in genres_related_to[book[2]][0]:
                            genres_related_to[book[2].strip()].append((book2[2].strip(), ImproperFrac(0, 0)))
                            genres_related_to[book[2].strip()][0].append(book2[2].strip())
            if type(book[2]) is tuple:
                for genre in book[2]:
                    if type(book2[2]) is tuple:
                        for genre2 in book2[2]:
                            if (genre.strip() == genre2.strip() and book[0] != book2[0]) and book2[0] not in \
                                    titles_related_to[book[0]][0]:
                                titles_related_to[book[0]].append((book2[0], ImproperFrac(0, 0)))
                                titles_related_to[book[0]][0].append(book2[0])
                                if book2[1] not in authors_related_to[book[1]][0]:
                                    authors_related_to[book[1]].append((book2[1], ImproperFrac(0, 0)))
                                    authors_related_to[book[1]][0].append(book2[1])

                    else:
                        if (genre.strip() == book2[2].strip() and book[0] != book2[0]) and book2[0] not in \
                                titles_related_to[book[0]][0]:
                            titles_related_to[book[0]].append((book2[0], ImproperFrac(0, 0)))
                            titles_related_to[book[0]][0].append(book2[0])
                            if book2[1] not in authors_related_to[book[1]][0]:
                                authors_related_to[book[1]].append((book2[1], ImproperFrac(0, 0)))
                                authors_related_to[book[1]][0].append(book2[1])
            else:
                if type(book2[2]) is tuple:
                    for genre2 in book2[2]:
                        if (book[2] == genre2.strip() and book[0] != book2[0]) and book2[0] not in \
                                titles_related_to[book[0]][0]:
                            titles_related_to[book[0]].append((book2[0], ImproperFrac(0, 0)))
                            titles_related_to[book[0]][0].append(book2[0])
                            if book2[1] not in authors_related_to[book[1]][0]:
                                authors_related_to[book[1]].append((book2[1], ImproperFrac(0, 0)))
                                authors_related_to[book[1]][0].append(book2[1])

                else:
                    if (book[2] == book2[2] and book[0] != book2[0]) and book2[0] not in \
                            titles_related_to[book[0]][0]:
                        titles_related_to[book[0]].append((book2[0], ImproperFrac(0, 0)))
                        titles_related_to[book[0]][0].append(book2[0])
                        if book2[1] not in authors_related_to[book[1]][0]:
                            authors_related_to[book[1]].append((book2[1], ImproperFrac(0, 0)))
                            authors_related_to[book[1]][0].append(book2[1])

for key, book in bookshelf.items():
    for word in word_tokenize(book[0]):
        if word not in wordset:
            continue
        for titleword in word_tokenize(book[0]):
            if titleword not in words_related_to[word][0] and titleword in wordset:
                words_related_to[word].append((titleword, ImproperFrac(0, 0)))
                words_related_to[word][0].append(titleword)
            if titleword.lower() not in words_related_to[word][0] and titleword.lower() in wordset:
                words_related_to[word].append((titleword.lower(), ImproperFrac(0, 0)))
                words_related_to[word][0].append(titleword.lower())
        for descriptionword in book[3]:
            if descriptionword not in words_related_to[word][0]:
                words_related_to[word].append((descriptionword, ImproperFrac(0, 0)))
                words_related_to[word][0].append(descriptionword)
            if descriptionword.lower() not in words_related_to[word][0]:
                words_related_to[word].append((descriptionword.lower(), ImproperFrac(0, 0)))
                words_related_to[word][0].append(descriptionword.lower())
        for genreword in book[2]:
            if genreword not in words_related_to[word][0] and genreword in wordset:
                words_related_to[word].append((genreword, ImproperFrac(0, 0)))
                words_related_to[word][0].append(genreword)
            if genreword.lower() not in words_related_to[word][0] and genreword.lower() in wordset:
                words_related_to[word].append((genreword.lower(), ImproperFrac(0, 0)))
                words_related_to[word][0].append(genreword.lower())
    if word.lower() in wordset:
        for titleword in word_tokenize(book[0]):
            if titleword not in words_related_to[word.lower()][0] and titleword in wordset:
                words_related_to[word.lower()].append((titleword, ImproperFrac(0, 0)))
                words_related_to[word.lower()][0].append(titleword)
            if titleword.lower() not in words_related_to[word.lower()][0] and titleword.lower() in wordset:
                words_related_to[word.lower()].append((titleword.lower(), ImproperFrac(0, 0)))
                words_related_to[word.lower()][0].append(titleword.lower())
        for descriptionword in book[3]:
            if descriptionword not in words_related_to[word.lower()][0]:
                words_related_to[word.lower()].append((descriptionword, ImproperFrac(0, 0)))
                words_related_to[word.lower()][0].append(descriptionword)
            if descriptionword.lower() not in words_related_to[word.lower()][0]:
                words_related_to[word.lower()].append((descriptionword.lower(), ImproperFrac(0, 0)))
                words_related_to[word.lower()][0].append(descriptionword.lower())
        for genreword in book[2]:
            if genreword not in words_related_to[word.lower()][0] and genreword in wordset:
                words_related_to[word.lower()].append((genreword, ImproperFrac(0, 0)))
                words_related_to[word.lower()][0].append(genreword)
            if genreword.lower() not in words_related_to[word.lower()][0] and genreword.lower() in wordset:
                words_related_to[word.lower()].append((genreword.lower(), ImproperFrac(0, 0)))
                words_related_to[word.lower()][0].append(genreword.lower())
    for description in book[3]:
        for titleword in word_tokenize(book[0]):
            if titleword not in words_related_to[description][0] and titleword in wordset:
                words_related_to[description].append((titleword, ImproperFrac(0, 0)))
                words_related_to[description][0].append(titleword)
            if titleword.lower() not in words_related_to[description][0] and titleword.lower() in wordset:
                words_related_to[description].append((titleword.lower(), ImproperFrac(0, 0)))
                words_related_to[description][0].append(titleword.lower())
        for descriptionword in book[3]:
            if descriptionword not in words_related_to[description][0] and descriptionword in wordset:
                words_related_to[description].append((descriptionword, ImproperFrac(0, 0)))
                words_related_to[description][0].append(descriptionword)
            if descriptionword.lower() not in words_related_to[description][0] and descriptionword.lower() in wordset:
                words_related_to[description].append((descriptionword.lower(), ImproperFrac(0, 0)))
                words_related_to[description][0].append(descriptionword.lower())
        for genreword in book[2]:
            if genreword not in words_related_to[description][0] and genreword in wordset:
                words_related_to[description].append((genreword, ImproperFrac(0, 0)))
                words_related_to[description][0].append(genreword)
            if genreword.lower() not in words_related_to[description][0] and genreword.lower() in wordset:
                words_related_to[description].append((genreword.lower(), ImproperFrac(0, 0)))
                words_related_to[description][0].append(genreword.lower())
    if description.lower() in wordset:
        for titleword in word_tokenize(book[0]):
            if titleword not in words_related_to[description.lower()][0] and titleword in wordset:
                words_related_to[description.lower()].append((titleword, ImproperFrac(0, 0)))
                words_related_to[description.lower()][0].append(titleword)
            if titleword.lower() not in words_related_to[description.lower()][
                0] and titleword.lower() in wordset:
                words_related_to[description.lower()].append((titleword.lower(), ImproperFrac(0, 0)))
                words_related_to[description.lower()][0].append(titleword.lower())
        for descriptionword in book[3]:
            if descriptionword not in words_related_to[description.lower()][0]:
                words_related_to[description.lower()].append((descriptionword, ImproperFrac(0, 0)))
                words_related_to[description.lower()][0].append(descriptionword)
            if descriptionword.lower() not in words_related_to[description.lower()][0]:
                words_related_to[description.lower()].append((descriptionword.lower(), ImproperFrac(0, 0)))
                words_related_to[description.lower()][0].append(descriptionword.lower())
        for genreword in book[2]:
            if genreword not in words_related_to[description.lower()][0] and genreword in wordset:
                words_related_to[description.lower()].append((genreword, ImproperFrac(0, 0)))
                words_related_to[description.lower()][0].append(genreword)
            if genreword.lower() not in words_related_to[description.lower()][
                0] and genreword.lower() in wordset:
                words_related_to[description.lower()].append((genreword.lower(), ImproperFrac(0, 0)))
                words_related_to[description.lower()][0].append(genreword.lower())
    for genre in book[2]:
        if genre in wordset:
            for titleword in word_tokenize(book[0]):
                if titleword not in words_related_to[genre][0] and titleword in wordset:
                    words_related_to[genre].append((titleword, ImproperFrac(0, 0)))
                    words_related_to[genre][0].append(titleword)
                if titleword.lower() not in words_related_to[genre][
                    0] and titleword.lower() in wordset:
                    words_related_to[genre].append((titleword.lower(), ImproperFrac(0, 0)))
                    words_related_to[genre][0].append(titleword.lower())
            for descriptionword in book[3]:
                if descriptionword not in words_related_to[genre][0]:
                    words_related_to[genre].append((descriptionword, ImproperFrac(0, 0)))
                    words_related_to[genre][0].append(descriptionword)
                if descriptionword.lower() not in words_related_to[genre][0]:
                    words_related_to[genre].append((descriptionword.lower(), ImproperFrac(0, 0)))
                    words_related_to[genre][0].append(descriptionword.lower())
            for genreword in book[2]:
                if genreword not in words_related_to[genre][0] and genreword in wordset:
                    words_related_to[genre].append((genreword, ImproperFrac(0, 0)))
                    words_related_to[genre][0].append(genreword)
                if genreword.lower() not in words_related_to[genre][
                    0] and genreword.lower() in wordset:
                    words_related_to[genre].append((genreword.lower(), ImproperFrac(0, 0)))
                    words_related_to[genre][0].append(genreword.lower())
        if genre.lower() in wordset:
            for titleword in word_tokenize(book[0]):
                if titleword not in words_related_to[genre.lower()][0] and titleword in wordset:
                    words_related_to[genre.lower()].append((titleword, ImproperFrac(0, 0)))
                    words_related_to[genre.lower()][0].append(titleword)
                if titleword.lower() not in words_related_to[genre.lower()][
                    0] and titleword.lower() in wordset:
                    words_related_to[genre.lower()].append((titleword.lower(), ImproperFrac(0, 0)))
                    words_related_to[genre.lower()][0].append(titleword.lower())
            for descriptionword in book[3]:
                if descriptionword not in words_related_to[genre.lower()][0]:
                    words_related_to[genre.lower()].append((descriptionword, ImproperFrac(0, 0)))
                    words_related_to[genre.lower()][0].append(descriptionword)
                if descriptionword.lower() not in words_related_to[genre.lower()][0]:
                    words_related_to[genre.lower()].append((descriptionword.lower(), ImproperFrac(0, 0)))
                    words_related_to[genre.lower()][0].append(descriptionword.lower())
            for genreword in book[2]:
                if genreword not in words_related_to[genre.lower()][0] and genreword in wordset:
                    words_related_to[genre.lower()].append((genreword, ImproperFrac(0, 0)))
                    words_related_to[genre.lower()][0].append(genreword)
                if genreword.lower() not in words_related_to[genre.lower()][
                    0] and genreword.lower() in wordset:
                    words_related_to[genre.lower()].append((genreword.lower(), ImproperFrac(0, 0)))
                    words_related_to[genre.lower()][0].append(genreword.lower())

# for key, title in titles_related_to.items():
#     #print(str(key) + str(title))
#     if len(title[0]) < 10:
#         print(str(key))
#         for element in sorted(title[0]):
#             print("\t" + element)

# for key, author in authors_related_to.items():
#     if len(author[0]) < 100:
#         print(str(key))
#         for element in sorted(author[0]):
#               print("\t"+element)

# for key, genre in genres_related_to.items():
#     if len(genre[0]) < 100:
#         print(str(key))
#         for element in sorted(genre[0]):
#                 print("\t"+element)

# for key, word in words_related_to.items():
#     if 1 < len(word[0]) < 60:
#         print(str(key))
#         for element in sorted(word[0]):
#             print("\t" + element)

for key, book in bookshelf.items():
    if type(book[2]) is tuple:
        for i in range(0, len(book[2])):
            for j in range(0, len(book[2])):
                if book[2][j] in genres_related_to[book[2][i].strip()][0]:
                    index = genres_related_to[book[2][i].strip()][0].index(str(book[2][j].strip()))
                    if book[2][j] != book[2][i]:
                        genres_related_to[book[2][i].strip()][index + 1][1].up_num()
                    else:
                        for k in range(1, len(genres_related_to[book[2][i].strip()])):
                            if k != (index + 1):
                                genres_related_to[book[2][i].strip()][k][1].up_den()
                        genres_related_to[book[2][i].strip()][index + 1][1].up_numden()
#NOT FOR GENRES FOR WORDS
# for i in range(0, len(words_related_to)):
#     for j in range(0, len(words_related_to)):
#         if book[2][j] in words_related_to[book[2][i].strip()][0]:
#             index = genres_related_to[book[2][i].strip()][0].index(str(book[2][j].strip()))
#             if book[2][j] != book[2][i]:
#                 genres_related_to[book[2][i].strip()][index + 1][1].up_num()
#             else:
#                 for k in range(1, len(genres_related_to[book[2][i].strip()])):
#                     if k != (index + 1):
#                         genres_related_to[book[2][i].strip()][k][1].up_den()
#                 genres_related_to[book[2][i].strip()][index + 1][1].up_numden()

for key, genre in genres_related_to.items():
    print(key)
    for i in range(1, len(genre)):
        print("\t" + str(genres_related_to[key][i]))

close_the_pickle_jar(bookshelf, wordset, authors_related_to, genres_related_to, titles_related_to, words_related_to,
                     bookDict, namedictionary, stopset, acceptablehyphens, unacceptablehyphens,
                     dictionary)
