import json
from pprint import pprint

with open('JsonDataTest.json') as data_file:
    data = json.load(data_file)

class Book:
    def __init__(self, json_entry):
        self.title = ""
        self.subtitle = ""
        self.authors = set()
        self.publisher = set()
        self.description = set()
        self.pageCount = 0
        self.genres = set()

        try:
            self.title = json_entry["title"]
        except KeyError:
            self.title = "N/A"

        try:
            self.subtitle = json_entry["subtitle"]
        except KeyError:
            self.subtitle = "N/A"

        try:
            self.publisher = json_entry["publisher"]
        except KeyError:
            self.publisher = "N/A"

        try:
            for authors in json_entry["authors"]:
                self.authors.add(authors)
        except KeyError:
            self.authors="N/A"

        # try:
        #     temp_wordlist = word_tokenize(json_entry["description"])
        #     for is_word in temp_wordlist:
        #         if is_word in word_list:
        #             self.description.add(is_word)
        # except KeyError:
        self.description = self.description.add("N/A")

        try:
            self.pageCount = json_entry["pageCount"]
        except KeyError:
            self.pageCount = "N/A"

        try:
            for genres in json_entry["categories"]:
                self.genres.add(genres)
        except KeyError:
            self.genres = "N/A"

    def __len__(self):
        return self.pageCount

    def __hash__(self):
        return hash(
            (str(self.publisher), str(self.pageCount), str(self.genres), str(self.authors), str(self.description),
             str(self.subtitle), str(self.title)))

    def __repr__(self):
        return str(self.title) + ": " + str(self.subtitle) + "\n\tAuthor(s): " + str(self.authors) + \
               "\n\tDescription: " + str(self.description) + "\n\tGenre(s): " + str(self.genres) + "\n\tPage Count: " + \
               str(self.pageCount) + "\n\tPublisher: " + str(self.publisher) + "\n"

    def __str__(self):
        return str(self.title) + ": " + str(self.subtitle) + "\n\tAuthor(s): " + str(self.authors) + \
               "\n\tDescription: " + str(self.description) + "\n\tGenre(s): " + str(self.genres) + "\n\tPage Count: " + \
               str(self.pageCount) + "\n\tPublisher: " + str(self.publisher) + "\n"

    def __ne__(self, other):
        return not (self == other)

    def __eq__(self, other):
        return (str(self.publisher), str(self.pageCount), str(self.genres), str(self.authors), str(self.description),
                str(self.subtitle), str(self.title)) == \
               (str(other.publisher), str(other.pageCount), str(other.genres), str(other.authors),
                str(other.description),
                str(other.subtitle), str(other.title))
k=0
for items in data["items"]:
    k+=1
print(k)