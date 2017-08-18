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

    def add_those_letters(self):
        # type: () -> object
        letter_sum = 0
        for letter in str(self.title):
            letter_sum += ord(letter)
        for letter in str(self.unititle):
            letter_sum += ord(letter)
        for letter in str(self.subject):
            letter_sum += ord(letter)
        for letter in str(self.language):
            letter_sum += ord(letter)
        for letter in str(self.publisher):
            letter_sum += ord(letter)
        for letter in str(self.creator):
            letter_sum += ord(letter)
        for letter in str(self.description):
            letter_sum += ord(letter)
        for letter in str(self.contributor):
            letter_sum += ord(letter)
        for letter in str(self.creationdate):
            letter_sum += ord(letter)
        for letter in str(self.formatt):
            letter_sum += ord(letter)
        for letter in str(self.identifier):
            letter_sum += ord(letter)
        for letter in str(self.source):
            letter_sum += ord(letter)
        for letter in str(self.typee):
            letter_sum += ord(letter)
        for letter in str(self.relation):
            letter_sum += ord(letter)
        for letter in str(self.lds01):
            letter_sum += ord(letter)
        for letter in str(self.lds02):
            letter_sum += ord(letter)
        for letter in str(self.lds04):
            letter_sum += ord(letter)
        for letter in str(self.lds05):
            letter_sum += ord(letter)
        for letter in str(self.lds08):
            letter_sum += ord(letter)
        for letter in str(self.lds10):
            letter_sum += ord(letter)
        for letter in str(self.lds11):
            letter_sum += ord(letter)
        for letter in str(self.lds12):
            letter_sum += ord(letter)
        for letter in str(self.lds13):
            letter_sum += ord(letter)
        for letter in str(self.lds33):
            letter_sum += ord(letter)
        for letter in str(self.lds34):
            letter_sum += ord(letter)
        for letter in str(self.lds35):
            letter_sum += ord(letter)
        for letter in str(self.lds37):
            letter_sum += ord(letter)
        return letter_sum

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


with open('BookDict.pkl', 'rb') as handle:
    dictionaryBook = pickle.load(handle)

print(len(dictionaryBook))
