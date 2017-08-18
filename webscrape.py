import hashlib

from bs4 import BeautifulSoup
import simplejson as json
import urllib.request
import pickle


class Book(object):
    title = ""
    unititle = ""
    subject = ""
    language = ""
    publisher = ""
    creator = ""
    description = ""
    contributor = ""
    creationdate = ""
    formatt = ""
    identifier = ""
    source = ""
    typee = ""
    relation = ""
    lds01 = ""
    lds02 = ""
    lds04 = ""
    lds05 = ""
    lds08 = ""
    lds10 = ""
    lds11 = ""
    lds12 = ""
    lds13 = ""
    lds33 = ""
    lds34 = ""
    lds35 = ""
    lds37 = ""
    lettersum = 0

    def __init__(self, title, unititle, subject, language, publisher,
                 creator, description, contributor, creationdate, formatt,
                 identifier, source, typee, relation, lds01, lds02,
                 lds04, lds05, lds08, lds10, lds11, lds12, lds13, lds33,
                 lds34, lds35, lds37):
        self.title = title
        self.unititle = unititle
        self.subject = subject
        self.language = language
        self.publisher = publisher
        self.creator = creator
        self.description = description
        self.contributor = contributor
        self.creationdate = creationdate
        self.formatt = formatt
        self.identifier = identifier
        self.source = source
        self.typee = typee
        self.relation = relation
        self.lds01 = lds01
        self.lds02 = lds02
        self.lds04 = lds04
        self.lds05 = lds05
        self.lds08 = lds08
        self.lds10 = lds10
        self.lds11 = lds11
        self.lds12 = lds12
        self.lds13 = lds13
        self.lds33 = lds33
        self.lds34 = lds34
        self.lds35 = lds35
        self.lds37 = lds37

    def add_those_letters(self, string1):
        # type: () -> object
        hash_object = hashlib.sha1(string1.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig

    # @property
    def __repr__(self):
        return "title= " + str(self.title) + "\n" + "unititle= " \
               + str(self.unititle) + "\n" + "subject= " + str(self.subject) \
               + "\n" + "language= " + str(self.language) + "\n" + "publisher= " \
               + str(self.publisher) + "\n" + "creator= " + str(self.creator) + "\n" + "description= " \
               + str(self.description) + "\n" + "contributor= " + str(self.contributor) + "\n" \
               + "creationdate= " + str(self.creationdate) + "\n" + "format= " + str(self.formatt) \
               + "\n" + "identifier= " + str(self.identifier) + "\n" + "source= " + str(self.source) \
               + "\n" + "type= " + str(self.typee) + "\n" + "relation= " + str(self.relation) \
               + "\n" + "lds01= " + str(self.lds01) + "\n" + "lds02= " + str(self.lds02) + "\n" \
               + "lds04= " + str(self.lds04) + "\n" + "lds05= " + str(self.lds05) + "\n" + \
               "lds08= " + str(self.lds08) + "\n" + "lds10= " + str(self.lds10) + "\n" \
               + "lds11= " + str(self.lds11) + "\n" + "lds12= " + str(self.lds12) + "\n" + "lds13= " \
               + str(self.lds13) + "\n" + "lds33= " + str(self.lds33) + "\n" + "lds34= " \
               + str(self.lds34) + "\n" + "lds35= " + str(self.lds35) + "\n" + "lds37= " + str(self.lds37)


try:
    with open('BookDict.pkl', 'rb') as handle:
        dictionaryBook = pickle.load(handle)
except EOFError:
    dictionaryBook = {}
try:
    with open('BookCreator.pkl', 'rb') as handle:
        creatorBook = pickle.load(handle)
except EOFError:
    creatorBook = {}
try:
    with open('BookTitle.pkl', 'rb') as handle:
        titleBook = pickle.load(handle)
except EOFError:
    titleBook = {}
try:
    with open('BookUnititle.pkl', 'rb') as handle:
        unititleBook = pickle.load(handle)
except EOFError:
    unititleBook = {}
try:
    with open('BookSubject.pkl', 'rb') as handle:
        subjectBook = pickle.load(handle)
except EOFError:
    subjectBook = {}
try:
    with open('BookLanguage.pkl', 'rb') as handle:
        languageBook = pickle.load(handle)
except EOFError:
    languageBook = {}
try:
    with open('BookPublisher.pkl', 'rb') as handle:
        publisherBook = pickle.load(handle)
except EOFError:
    publisherBook = {}
try:
    with open('BookDescription.pkl', 'rb') as handle:
        descriptionBook = pickle.load(handle)
except EOFError:
    descriptionBook = {}
try:
    with open('BookContributor.pkl', 'rb') as handle:
        contributorBook = pickle.load(handle)
except EOFError:
    contributorBook = {}
try:
    with open('BookCreationDate.pkl', 'rb') as handle:
        creationdateBook = pickle.load(handle)
except EOFError:
    creationdateBook = {}
try:
    with open('BookFormat.pkl', 'rb') as handle:
        formatBook = pickle.load(handle)
except EOFError:
    formatBook = {}
try:
    with open('BookIdentifier.pkl', 'rb') as handle:
        identifierBook = pickle.load(handle)
except EOFError:
    identifierBook = {}
try:
    with open('BookSource.pkl', 'rb') as handle:
        sourceBook = pickle.load(handle)
except EOFError:
    sourceBook = {}
try:
    with open('BookType.pkl', 'rb') as handle:
        typeBook = pickle.load(handle)
except EOFError:
    typeBook = {}
try:
    with open('BookRelation.pkl', 'rb') as handle:
        relationBook = pickle.load(handle)
except EOFError:
    relationBook = {}
try:
    with open('BookLDS01.pkl', 'rb') as handle:
        lds01Book = pickle.load(handle)
except EOFError:
    lds01Book = {}
try:
    with open('BookLDS02.pkl', 'rb') as handle:
        lds02Book = pickle.load(handle)
except EOFError:
    lds02Book = {}
try:
    with open('BookLDS04.pkl', 'rb') as handle:
        lds04Book = pickle.load(handle)
except EOFError:
    lds04Book = {}
try:
    with open('BookLDS05.pkl', 'rb') as handle:
        lds05Book = pickle.load(handle)
except EOFError:
    lds05Book = {}
try:
    with open('BookLDS08.pkl', 'rb') as handle:
        lds08Book = pickle.load(handle)
except EOFError:
    lds08Book = {}
try:
    with open('BookLDS10.pkl', 'rb') as handle:
        lds10Book = pickle.load(handle)
except EOFError:
    lds10Book = {}
try:
    with open('BookLDS11.pkl', 'rb') as handle:
        lds11Book = pickle.load(handle)
except EOFError:
    lds11Book = {}
try:
    with open('BookLDS12.pkl', 'rb') as handle:
        lds12Book = pickle.load(handle)
except EOFError:
    lds12Book = {}
try:
    with open('BookLDS13.pkl', 'rb') as handle:
        lds13Book = pickle.load(handle)
except EOFError:
    lds13Book = {}
try:
    with open('BookLDS33.pkl', 'rb') as handle:
        lds33Book = pickle.load(handle)
except EOFError:
    lds33Book = {}
try:
    with open('BookLDS33.pkl', 'rb') as handle:
        lds33Book = pickle.load(handle)
except EOFError:
    lds33Book = {}
try:
    with open('BookLDS34.pkl', 'rb') as handle:
        lds34Book = pickle.load(handle)
except EOFError:
    lds34Book = {}
try:
    with open('BookLDS35.pkl', 'rb') as handle:
        lds35Book = pickle.load(handle)
except EOFError:
    lds35Book = {}
try:
    with open('BookLDS37.pkl', 'rb') as handle:
        lds37Book = pickle.load(handle)
except EOFError:
    lds37Book = {}



def partition(array, begin, end):
    pivot = begin
    for si in range(begin + 1, end + 1):
        if array[si] <= array[begin]:
            pivot += 1
            array[si], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot - 1)
    quicksort(array, pivot + 1, end)


#
#
# def sort_nums():
#     names_list = filter(None, open("bookNums.txt", "r").read().splitlines())
#     i = 0
#     for line in names_list:
#         names_list[i] = int(line)
#         i += 1
#     quicksort(names_list)
#     g = open('bookNums.txt', 'w')
#     g.truncate()
#     for lines in names_list:
#         g.write(str(lines) + "\n")
#     g.close()


def clean_up_file(filename):
    names_list = filter(None, open(filename, "r").read().splitlines())
    g = open(filename, 'w')
    g.truncate()
    for lines in names_list:
        if lines != "No Information":
            g.write(str(lines) + "\n")
    g.close()


def write_to_file(book_to_save, num):
    # f = open('bookNums.txt', 'r')

    write_to_full = open("bookData2.txt", 'a')
    write_to_num = open("bookNums2.txt", 'a')
    write_to_title = open("bookTitle2.txt", 'a')
    write_to_creator = open("bookCreator2.txt", 'a')
    write_to_identifier = open("bookIdentifier2.txt", 'a')

    # line = f.readline()
    # while line:
    #     if book_to_save.add_those_letters() == line:
    #         print ("ERROR WILL ROBINSON")
    #         return
    #     line = f.readline()

    write_to_full.write(str(num) + "\n" + str(book_to_save) + "\n" + "\n")
    write_to_num.write(str(book_to_save.add_those_letters()) + "\n")
    write_to_title.write(str(book_to_save.title) + "\n")
    write_to_creator.write(str(book_to_save.creator) + "\n")
    write_to_identifier.write(str(book_to_save.identifier) + "\n")

    # f.close()

    write_to_full.close()
    write_to_num.close()
    write_to_title.close()
    write_to_creator.close()
    write_to_identifier.close()


for i in range(20):
    r = urllib.request.urlopen('http://library.lclark.edu/testpages/get_random.php?limit=100').read()

    soup = BeautifulSoup(r, "html.parser")
    print(type(soup))

    soup = str(soup)
    soup = soup[1:]

    jsondata = soup.split("{\"type")

    for s in range(1, len(jsondata)):

        try:
            if "}]" not in jsondata[s]:
                jsondata[s] = "{\"type" + jsondata[s]
                jsondata[s] = jsondata[s][0:-1]
                parsedjson = json.loads(jsondata[s])
                # print parsedjson
                try:
                    booktitle = str(parsedjson['title'])
                except (NameError, KeyError, TypeError):
                    booktitle = "No Information"
                try:
                    bookunititle = str(parsedjson['unititle'])
                except (NameError, KeyError, TypeError):
                    bookunititle = "No Information"
                try:
                    booksubject = str(parsedjson['subject'])
                except (NameError, KeyError, TypeError):
                    booksubject = "No Information"
                try:
                    booklanguage = str(parsedjson['language'])
                except (NameError, KeyError, TypeError):
                    booklanguage = "No Information"
                try:
                    bookpublisher = str(parsedjson['publisher'])
                except (NameError, KeyError, TypeError):
                    bookpublisher = "No Information"
                try:
                    bookcreator = str(parsedjson['creator'])
                except (NameError, KeyError, TypeError):
                    bookcreator = "No Information"
                try:
                    bookdescription = str(parsedjson['description'])
                except (NameError, KeyError, TypeError):
                    bookdescription = "No Information"
                try:
                    bookcontributor = str(parsedjson['contributor'])
                except (NameError, KeyError, TypeError):
                    bookcontributor = "No Information"
                try:
                    bookcreationdate = str(parsedjson['creationdate'])
                except (NameError, KeyError, TypeError):
                    bookcreationdate = "No Information"
                try:
                    bookformat = str(parsedjson['format'])

                except (NameError, KeyError, TypeError):
                    bookformat = "No Information"
                try:
                    bookidentifier = str(parsedjson['identifier'])
                    bookidentifier = bookidentifier.replace("$$CISBN$$V", "")
                except (NameError, KeyError, TypeError):
                    bookidentifier = "No Information"
                try:
                    booksource = str(parsedjson['source'])
                except (NameError, KeyError, TypeError):
                    booksource = "No Information"
                try:
                    booktype = str(parsedjson['type'])
                except (NameError, KeyError, TypeError):
                    booktype = "No Information"
                try:
                    bookrelation = str(parsedjson['relation'])
                except (NameError, KeyError, TypeError):
                    bookrelation = "No Information"
                try:
                    booklds01 = str(parsedjson['lds01'])
                except (NameError, KeyError, TypeError):
                    booklds01 = "No Information"
                try:
                    booklds02 = str(parsedjson['lds02'])
                except (NameError, KeyError, TypeError):
                    booklds02 = "No Information"
                try:
                    booklds04 = str(parsedjson['lds04'])
                except (NameError, KeyError, TypeError):
                    booklds04 = "No Information"
                try:
                    booklds05 = str(parsedjson['lds05'])
                except (NameError, KeyError, TypeError):
                    booklds05 = "No Information"
                try:
                    booklds08 = str(parsedjson['lds08'])
                except (NameError, KeyError, TypeError):
                    booklds08 = "No Information"
                try:
                    booklds10 = str(parsedjson['lds10'])
                except (NameError, KeyError, TypeError):
                    booklds10 = "No Information"
                try:
                    booklds11 = str(parsedjson['lds11'])
                except (NameError, KeyError, TypeError):
                    booklds11 = "No Information"
                try:
                    booklds12 = str(parsedjson['lds12'])
                except (NameError, KeyError, TypeError):
                    booklds12 = "No Information"
                try:
                    booklds13 = str(parsedjson['lds13'])
                except (NameError, KeyError, TypeError):
                    booklds13 = "No Information"
                try:
                    booklds33 = str(parsedjson['lds33'])
                except (NameError, KeyError, TypeError):
                    booklds33 = "No Information"
                try:
                    booklds34 = str(parsedjson['lds34'])
                except (NameError, KeyError, TypeError):
                    booklds34 = "No Information"
                try:
                    booklds35 = str(parsedjson['lds35'])
                except (NameError, KeyError, TypeError):
                    booklds35 = "No Information"
                try:
                    booklds37 = str(parsedjson['lds37'])
                except (NameError, KeyError, TypeError):
                    booklds37 = "No Information"
                book = Book(booktitle, bookunititle, booksubject, booklanguage, bookpublisher, bookcreator,
                            bookdescription,
                            bookcontributor, bookcreationdate, bookformat, bookidentifier, booksource, booktype,
                            bookrelation, booklds01, booklds02, booklds04, booklds05, booklds08, booklds10, booklds11,
                            booklds12, booklds13, booklds33, booklds34, booklds35, booklds37)
                #print(book)
                dictionaryBook[book.add_those_letters(str(book))] = book
                creatorBook[book.add_those_letters(str(book))] = book.creator
                titleBook[book.add_those_letters(str(book))] = book.title
                unititleBook[book.add_those_letters(str(book))] = book.unititle
                subjectBook[book.add_those_letters(str(book))] = book.subject
                languageBook[book.add_those_letters(str(book))] = book.language
                publisherBook[book.add_those_letters(str(book))] = book.publisher
                descriptionBook[book.add_those_letters(str(book))] = book.description
                contributorBook[book.add_those_letters(str(book))] = book.contributor
                creationdateBook[book.add_those_letters(str(book))] = book.creationdate
                formatBook[book.add_those_letters(str(book))] = book.formatt
                identifierBook[book.add_those_letters(str(book))] = book.identifier
                sourceBook[book.add_those_letters(str(book))] = book.source
                typeBook[book.add_those_letters(str(book))] = book.typee
                relationBook[book.add_those_letters(str(book))] = book.relation
                lds01Book[book.add_those_letters(str(book))] = book.lds01
                lds02Book[book.add_those_letters(str(book))] = book.lds02
                lds04Book[book.add_those_letters(str(book))] = book.lds04
                lds05Book[book.add_those_letters(str(book))] = book.lds05
                lds08Book[book.add_those_letters(str(book))] = book.lds08
                lds10Book[book.add_those_letters(str(book))] = book.lds10
                lds11Book[book.add_those_letters(str(book))] = book.lds11
                lds12Book[book.add_those_letters(str(book))] = book.lds12
                lds13Book[book.add_those_letters(str(book))] = book.lds13
                lds33Book[book.add_those_letters(str(book))] = book.lds33
                lds34Book[book.add_those_letters(str(book))] = book.lds34
                lds35Book[book.add_those_letters(str(book))] = book.lds35
                lds37Book[book.add_those_letters(str(book))] = book.lds37


        except ValueError:
            print("error at jsondata[" + str(s) + "]")
            print(jsondata[s])
            continue

        import pickle

    with open('BookDict.pkl', 'wb') as handle:
        pickle.dump(dictionaryBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookCreator.pkl', 'wb') as handle:
        pickle.dump(creatorBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookTitle.pkl', 'wb') as handle:
        pickle.dump(titleBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookUnititle.pkl', 'wb') as handle:
        pickle.dump(unititleBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookSubject.pkl', 'wb') as handle:
        pickle.dump(subjectBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLanguage.pkl', 'wb') as handle:
        pickle.dump(languageBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookPublisher.pkl', 'wb') as handle:
        pickle.dump(publisherBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookDescription.pkl', 'wb') as handle:
        pickle.dump(descriptionBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookContributor.pkl', 'wb') as handle:
        pickle.dump(contributorBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookCreationDate.pkl', 'wb') as handle:
        pickle.dump(creationdateBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookFormat.pkl', 'wb') as handle:
        pickle.dump(formatBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookIdentifier.pkl', 'wb') as handle:
        pickle.dump(identifierBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookSource.pkl', 'wb') as handle:
        pickle.dump(sourceBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookType.pkl', 'wb') as handle:
        pickle.dump(typeBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookRelation.pkl', 'wb') as handle:
        pickle.dump(relationBook, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS01.pkl', 'wb') as handle:
        pickle.dump(lds01Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS02.pkl', 'wb') as handle:
        pickle.dump(lds02Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS04.pkl', 'wb') as handle:
        pickle.dump(lds04Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS05.pkl', 'wb') as handle:
        pickle.dump(lds05Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS08.pkl', 'wb') as handle:
        pickle.dump(lds08Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS10.pkl', 'wb') as handle:
        pickle.dump(lds10Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS11.pkl', 'wb') as handle:
        pickle.dump(lds10Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS12.pkl', 'wb') as handle:
        pickle.dump(lds10Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS13.pkl', 'wb') as handle:
        pickle.dump(lds10Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS33.pkl', 'wb') as handle:
        pickle.dump(lds10Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS34.pkl', 'wb') as handle:
        pickle.dump(lds10Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS35.pkl', 'wb') as handle:
        pickle.dump(lds10Book, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('BookLDS37.pkl', 'wb') as handle:
        pickle.dump(lds10Book, handle, protocol=pickle.HIGHEST_PROTOCOL)