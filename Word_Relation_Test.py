import operator
import pickle
import random
import string
import math
from math import *
from pprint import pprint
import json
import nltk
import numpy
from nltk import word_tokenize, re
from graphics import *

with open('Book_Pickles/SampleDict.pkl', 'rb') as handle:
    bookshelf = pickle.load(handle)
with open('Text_Pickles/stopwords.pkl', 'rb') as handle:
    stopwords = pickle.load(handle)
with open('Text_Pickles/AcceptableHyphens.pkl', 'rb') as handle:
    acceptable_hyphens = pickle.load(handle)
with open('Text_Pickles/UnacceptableHyphens.pkl', 'rb') as handle:
    unacceptable_hyphens = pickle.load(handle)
with open('Text_Pickles/Replacements.pkl', 'rb') as handle:
    replacements = pickle.load(handle)
with open('Text_Pickles/Irreplacements.pkl', 'rb') as handle:
    irreplacements = pickle.load(handle)
with open('JsonDataTest.json') as data_file:
    data = json.load(data_file)
with open('Text_Pickles/Dictionary.pkl', 'rb') as handle:
    sample_dict = pickle.load(handle)


class EmptyException(Exception):
    pass


class Comp_Table:
    def __init__(self, wordlist):
        self.wordlist = set(wordlist)
        self.table = {}
        for word in wordlist:
            if type(word) is str:
                self.table[word] = {}
                self.table[word][word] = 1
            if type(word) is Word:
                self.table[word] = {}
                self.table[word][word] = word.weight

    def __len__(self):
        return len(self.wordlist)

    def __hash__(self):
        return hash((str(self.wordlist), str(self.table)))

    def __repr__(self):
        return pprint.pformat(self.table)

    def __str__(self):
        return pprint.pformat(self.table)

    def __ne__(self, other):
        return not (self == other)

    def __eq__(self, other):
        return (self.table, self.wordlist) == (other.table, other.wordlist)

    def ordered_relations(self, word):
        ordered_relations = sorted(self.table[word].items(), key=operator.itemgetter(1))
        return ordered_relations


class Relationship_Map:
    def __init__(self, dict_of_words, desc_dict_map, book_author_genre):
        self.word_set = set(dict_of_words.keys())
        self.location_list = desc_dict_map
        self.ref_dict = dict_of_words
        self.word_coord = {}
        self.book_author_genre = book_author_genre

        sq_len = floor(729 / (floor(math.sqrt(len(dict_of_words)))))

        x = y = sq_len * .5
        for words in sorted(dict_of_words.keys()):

            # Record coordinates of word (randomly distributed)
            if x < 729:
                self.word_coord[dict_of_words[words].name] = Point(floor(x), floor(y))
                self.word_coord[Point(floor(x), floor(y))] = dict_of_words[words].name
                print(str(dict_of_words[words].name) + "---(" + str(x) + "," + str(y) + ")")
                x += sq_len
                continue
            elif x >= 729:
                x = sq_len * .5
                y += sq_len
                self.word_coord[dict_of_words[words].name] = Point(floor(x), floor(y))
                self.word_coord[Point(floor(x), floor(y))] = dict_of_words[words].name
                print(str(dict_of_words[words].name) + "---(" + str(x) + "," + str(y) + ")")
                x += sq_len
                continue

        self.title_comp_table = Comp_Table(sorted(self.location_list))
        self.word_comp_table = Comp_Table(sorted(self.ref_dict))

    def __len__(self):
        # Returns the number of words in wordlist
        return len(self.word_set)

    def __hash__(self):
        return hash(
            (str(self.word_set), str(self.location_list), str(self.ref_dict), str(self.word_coord)))

    def __repr__(self):
        return str(self.ref_dict)

    def __str__(self):
        return str(self.ref_dict)

    def __ne__(self, other):
        return not (self == other)

    def __eq__(self, other):
        return (self.ref_dict, self.location_list, self.word_set, self.word_coord) == (
            other.ref_dict, other.location_list, other.word_list, other.word_coord)

    def one_relations(self):
        k = 0
        for word1 in self.word_set:
            print(100 * k / len(self.word_set))
            k += 1
            for word2 in self.word_set:
                overlap = 0
                for loc in self.ref_dict[word2].locations:
                    if word1 in self.location_list[loc]:
                        overlap += 1
                if overlap > 0:
                    self.word_comp_table.table[word1][word2] = (len(self.ref_dict[word1]) / overlap) * self.ref_dict[
                        word1].weight * self.ref_dict[word2].weight

    def dijkstra(self, source_word):
        distance_to = {}
        graph = {}

        for words in sorted(self.word_set):
            distance_to[words] = float('inf')
            try:
                graph[words] = self.word_comp_table.table[source_word][words]
            except KeyError:
                graph[words] = float('inf')
        while graph:
            current_node = min(graph.items(), key=lambda x: x[1])
            if current_node[0] in graph.keys():
                del graph[current_node[0]]

                for neighbor in self.word_comp_table.table[current_node[0]].keys():
                    if distance_to[neighbor] > 1000:
                        test_dist = self.word_comp_table.table[current_node[0]][neighbor]
                    else:
                        test_dist = distance_to[neighbor] + self.word_comp_table.table[current_node[0]][neighbor]
                    if test_dist < distance_to[neighbor]:
                        distance_to[neighbor] = test_dist
                        try:
                            graph[neighbor] = test_dist
                        except KeyError:
                            continue
        for word2 in distance_to.keys():
            self.word_comp_table.table[source_word][word2] = distance_to[word2]

    # draws and maps all initial paths
    def draw_map(self):
        # See code above for explanation of math
        sq_len = floor(729 / (floor(math.sqrt(len(self.ref_dict)))))

        # Create window with extra width for text displays
        win = GraphWin("", 950, 729 + sq_len)

        # Create 4 text boxes: "Commandline", word displays and a troubleshooting box for displaying whatever necessecary
        text = Text(Point(835, 180), "Word 1")
        text.draw(win)
        word1box = Entry(Point(835, 200), 20)
        word1box.draw(win)

        text = Text(Point(835, 280), "Word 2")
        text.draw(win)
        word2box = Entry(Point(835, 300), 20)
        word2box.draw(win)

        text = Text(Point(835, 380), "Troubleshooting Printout")
        text.draw(win)
        ts_print = Entry(Point(835, 400), 20)
        ts_print.draw(win)

        text = Text(Point(835, 80), "Commandline")
        text.draw(win)
        inputbox = Entry(Point(835, 100), 20)
        inputbox.draw(win)

        textbox = Rectangle(Point(775, 715), Point(895, 500))
        textbox.setFill(color_rgb(211, 211, 215))
        textbox.draw(win)
        text = Text(Point(835, 510), "/q = quit")
        text.draw(win)
        text = Text(Point(835, 540), "/2w = 2-word relations")
        text.draw(win)
        text = Text(Point(835, 580), "/1w = 1-word relations")
        text.draw(win)
        text = Text(Point(835, 620), "/w = paths for one word")
        text.draw(win)
        text = Text(Point(835, 660), "/aw = all relations")
        text.draw(win)
        text = Text(Point(835, 700), "/cw = all paths")
        text.draw(win)
        g = ""

        # Based on the coordinates calculated in the init func, draw all points
        for word_points in self.word_coord:
            if type(word_points) is str:
                g = inputbox.getText()
                if g == "/q":
                    sys.exit(0)
                pt = self.word_coord[word_points]
                pt.draw(win)
                # cir = Circle(pt,sq_len*.5)
                # cir.draw(win)

        # Create circle list and line list, to keep track of previously drawn circles and lines
        # Both lists contain dummy variables to not screw up code below
        # Doesn't matter what they are so long as cir_list take the format [((Word,Point),Circle),((Word,Point),Circle)]
        cir_list = [Circle(Point(0, 0), 1), Circle(Point(0, 0), 1)]
        cir_index = False
        line = Line(Point(0, 0), Point(0, 0))
        undraw_list = [line]
        title_check = False

        while g != "/q":
            # Find mouse click coordinates, then check g for instructions
            f = win.getMouse()
            search_coord = Point(f.getX(), f.getY())
            g = inputbox.getText()

            # Clear line from last time
            for undraws in undraw_list:
                undraws.undraw()
            undraw_list = [Line(Point(0, 0), Point(0, 0))]

            for word_points in self.word_coord:
                # If mouse click within bouding box of points (i.e. pt + or -  radius)
                if type(word_points) is str:
                    if (search_coord.getX() <= (self.word_coord[word_points].getX() + sq_len * .5)) and (
                                search_coord.getX() >= (self.word_coord[word_points].getX() - sq_len * .5)) \
                            and (search_coord.getY() <= (self.word_coord[word_points].getY() + sq_len * .5)) and (
                                search_coord.getY() >= (self.word_coord[word_points].getY() - sq_len * .5)):

                        # Draw circle at clicked point
                        cir = Circle(self.word_coord[word_points], sq_len * .5)
                        cir.setFill(color_rgb(255, 223, 0))
                        cir.draw(win)

                        # Clears 2nd most previous circle
                        cir_list[int(cir_index)].undraw()
                        cir_list[int(cir_index)] = cir
                        cir_index = not cir_index

                        # Displays word name
                        if cir_index:
                            word1box.setText(word_points)
                            break
                        else:
                            word2box.setText(word_points)
                            break

            if g == "/w":
                ts_print.setText("Enter word")
                f = win.getMouse()
                self.one_relations()
                self.word_comp_table.ordered_relations("raise")
            if g == "/draw_title":
                tsq_len = floor(729 / (floor(math.sqrt(len(self.location_list)))))
                # Create window with extra width for text displays
                title_win = GraphWin("Title Window", 800, 729 + sq_len)
                title_coord = {}
                x = y = tsq_len * .5
                for title in sorted(self.location_list.keys()):
                    if x < 729:
                        title_coord[title] = Point(floor(x), floor(y))
                        title_coord[Point(floor(x), floor(y))] = title
                        print(str(title) + "---(" + str(x) + "," + str(y) + ")")
                        x += tsq_len
                        continue
                    elif x >= 729:
                        x = tsq_len * .5
                        y += tsq_len
                        title_coord[title] = Point(floor(x), floor(y))
                        title_coord[Point(floor(x), floor(y))] = title
                        print(str(title) + "---(" + str(x) + "," + str(y) + ")")
                        x += tsq_len

                        continue
                for title_points in title_coord:
                    if type(title_points) is str:
                        g = inputbox.getText()
                        if g == "/q":
                            sys.exit(0)
                        pt = title_coord[title_points]
                        pt.draw(title_win)
                        # cir = Circle(pt,sq_len*.5)
                        # cir.draw(win)

                # Create circle list and line list, to keep track of previously drawn circles and lines
                # Both lists contain dummy variables to not screw up code below
                # Doesn't matter what they are so long as cir_list take the format [((Word,Point),Circle),((Word,Point),Circle)]
                title_line = Line(Point(0, 0), Point(0, 0))
                title_undraw_list = [title_line]

                while g != "/tq":
                    # Find mouse click coordinates, then check g for instructions
                    f = title_win.getMouse()
                    title_search_coord = Point(f.getX(), f.getY())
                    g = inputbox.getText()

                    # Clear line from last time
                    for undraws in title_undraw_list:
                        undraws.undraw()
                    title_undraw_list = [Line(Point(0, 0), Point(0, 0))]

                    for title_points in title_coord:
                        # If mouse click within bouding box of points (i.e. pt + or -  radius)
                        if type(title_points) is str:
                            if (title_search_coord.getX() <= (title_coord[title_points].getX() + sq_len * .5)) and (
                                        title_search_coord.getX() >= (title_coord[title_points].getX() - sq_len * .5)) \
                                    and (title_search_coord.getY() <= (
                                                title_coord[title_points].getY() + sq_len * .5)) and (
                                        title_search_coord.getY() >= (title_coord[title_points].getY() - sq_len * .5)):

                                # Draw circle at clicked point
                                cir = Circle(title_coord[title_points], sq_len * .5)
                                cir.setFill(color_rgb(255, 223, 0))
                                cir.draw(title_win)
                                title_undraw_list.append(cir)
                                word1box.setText(title_points)

                                for loc in self.title_comp_table.table[title_points]:
                                    connecting_line = Line(title_coord[title_points], title_coord[loc])
                                    color_weight = int(
                                        -1 * math.exp(.001 * self.title_comp_table.table[title_points][loc]) + 255)
                                    line_color = color_rgb(255, color_weight, color_weight)
                                    connecting_line.setFill(line_color)
                                    connecting_line.draw(title_win)
                                    title_undraw_list.append(connecting_line)
                                break
                title_win.close()

            if g == "/title" and not title_check:
                cir_index = not cir_index
                self.one_relations()
                k = 0
                for word in self.word_set:
                    print(100 * k / len(self.word_set))
                    k += 1
                    self.dijkstra(word)

                avg_length = 0
                for title in self.location_list:
                    avg_length += len(self.location_list[title])
                avg_length / len(self.location_list)
                for title1 in self.location_list:
                    for title2 in self.location_list:
                        total_weight = 0
                        for word1 in self.location_list[title1]:
                            for word2 in self.location_list[title2]:
                                total_weight += self.word_comp_table.table[word1][word2]
                        b = 0.9
                        normalized_weight = 1 - b + (b * (len(self.location_list[title2]) / avg_length))

                        self.title_comp_table.table[title1][title2] = math.floor(
                            100000 * total_weight / normalized_weight) / 100000
                        if self.book_author_genre[title1]["description"] == "N/A" or self.book_author_genre[title2][
                            "description"] == "N/A":
                            self.title_comp_table.table[title1][title2] = float('inf')
                            print(title1)
                            print(title2)

                        if title1 == title2:
                            self.title_comp_table.table[title1][title2] = 0

                        if self.book_author_genre[title1]["authors"] != "N/A" and self.book_author_genre[title2][
                            "authors"] != "N/A":
                            if type(self.book_author_genre[title1]["authors"]) is list:
                                for authors1 in self.book_author_genre[title1]:
                                    if type(self.book_author_genre[title2]["authors"]) is list:
                                        for authors2 in self.book_author_genre[title2]:
                                            if authors1 == authors2:
                                                self.title_comp_table.table[title1][title2] *= .5
                                    else:
                                        if authors1 == self.book_author_genre[title2]["authors"]:
                                            self.title_comp_table.table[title1][title2] *= .5
                            else:
                                if type(self.book_author_genre[title2]["authors"]) is list:
                                    for authors2 in self.book_author_genre[title2]:
                                        if self.book_author_genre[title2]["authors"] == authors2:
                                            self.title_comp_table.table[title1][title2] *= .5
                                else:
                                    if self.book_author_genre[title2]["authors"] == self.book_author_genre[title2][
                                        "authors"]:
                                        self.title_comp_table.table[title1][title2] *= .5
                        if self.book_author_genre[title1]["genres"] != "N/A" and self.book_author_genre[title2][
                            "genres"] != "N/A":
                            if type(self.book_author_genre[title1]["genres"]) is list:
                                for genres1 in self.book_author_genre[title1]:
                                    if type(self.book_author_genre[title2]["genres"]) is list:
                                        for genres2 in self.book_author_genre[title2]:
                                            if genres1 == genres2:
                                                self.title_comp_table.table[title1][title2] *= .9
                                    else:
                                        if genres1 == self.book_author_genre[title2]["genres"]:
                                            self.title_comp_table.table[title1][title2] *= .9
                            else:
                                if type(self.book_author_genre[title2]["genres"]) is list:
                                    for genres2 in self.book_author_genre[title2]:
                                        if self.book_author_genre[title2]["genres"] == genres2:
                                            self.title_comp_table.table[title1][title2] *= .9
                                else:
                                    if self.book_author_genre[title2]["genres"] == self.book_author_genre[title2][
                                        "genres"]:
                                        self.title_comp_table.table[title1][title2] *= .9

                for title1 in sorted(self.title_comp_table.table.keys()):
                    print()
                    print(title1)
                    temp_dict = self.title_comp_table.table[title1]
                    sorted_dict = sorted(temp_dict.items(), key=operator.itemgetter(1))
                    for element in sorted_dict:
                        print("\t" + str(element[0]) + ": " + str(element[1]))
                title_check = True


class Word:
    def __init__(self, word):
        self.locations = set()
        self.weight = 0
        self.name = word

    def __len__(self):
        return len(self.name)

    def __hash__(self):
        return hash(
            (str(self.locations), self.name, str(self.weight)))

    def __repr__(self):
        return str(self.name) + "\n\tLocations: " + str(self.locations) + "\n\tWeight: " + str(self.weight)

    def __str__(self):
        return str(self.name) + "\n\tLocations: " + str(self.locations) + "\n\tWeight: " + str(self.weight)

    def __ne__(self, other):
        return not (self == other)

    def __eq__(self, other):
        return (self.name, self.locations, self.weight) == \
               (other.name, other.locations, other.weight)

    def share_roots(self):
        # Check word against combinations of prefix and suffix
        suff_list = ["able", "al", "ed", "ern", "es", "ess", "est", "ful", "hood", "ibly", "ing", "ish", "ive", "less",
                     "like",
                     "ling", "ly", "ment", "ness", "ous", "phile", "'s", "’s", "ship", "ward", "wise", "y", "’",
                     "'", "”", '"']
        pref_list = ["anti", "bi", "counter", "crypto", "de", "dis", "ecto", "ex-", "ex—", "exo", "extra", "in",
                     "inter", "intra", "ir", "kilo", "mega", "meta", "micro", "mis", "multi", "non", "now-", "now—",
                     "post", "re", "sub", "trans", "ultra", "un", "‘", "'", "—", "“", '"']
        return_word = self.name
        for suff in suff_list:
            for pref in pref_list:
                if (self.name.endswith(suff) and self.name.startswith(pref)) and \
                                self.name[len(pref):-(len(suff))] in sample_dict:
                    return_word = self.name[len(pref):-(len(suff))]
                    break

                if self.name.endswith(suff) and self.name[:-(len(suff))] in sample_dict:
                    return_word = self.name[:-(len(suff))]
                    break

                if self.name.startswith(pref) and self.name[len(pref):] in sample_dict:
                    return_word = self.name[len(pref):]
                    break
        if return_word not in stopwords:
            return return_word
        else:
            return self.name


def dictionary_questions(word, desc):
    if (word in stopwords or word.isdigit()) and word in desc_temp:
        desc_temp.remove(word)
    if re.search(r'^\W', word) and word in desc_temp:
        desc_temp.remove(word)
        desc_temp.append(word[1:])
        dictionary_questions(word[1:], desc_temp)
    if re.search(r'\W$', word) and word in desc_temp:
        desc_temp.remove(word)
        desc_temp.append(word[:len(word) - 1])
        dictionary_questions(word[:len(word) - 1], desc_temp)
    for remove in ["“", " ", ".”", "…", "'s", "’s", "‘", ".’", "“", "•", "+", "*"]:
        if word in desc_temp:
            desc_temp.remove(word)
            desc_temp.append(word.replace(remove, ""))

    for remove in ["-", "—", "-", "'", ",", ".", "/", "‘", "“", "•", "+", "*"]:
        if word.startswith(remove) and word in desc_temp:
            desc_temp.remove(word)
            new_word = word[1:]
            desc_temp.append(new_word)
    for remove in ["-", "—", "-", "'", ",", ".", "/", "‘", "“", "•", "+", "*"]:
        if word.endswith(remove) and word in desc_temp:
            desc_temp.remove(word)
            new_word = word[:-1]
            desc_temp.append(new_word)
    if word in unacceptable_hyphens and word in desc_temp:
        desc_temp.remove(word)
        if word.__contains__("-"):
            new_word = word.split("-")
            for sub_word in new_word:
                dictionary_questions(sub_word, desc_temp)
        if word.__contains__("—"):
            new_word = word.split("—")
            for sub_word in new_word:
                dictionary_questions(sub_word, desc_temp)
    if word.__contains__(
            "-") and word not in acceptable_hyphens and word not in unacceptable_hyphens and word not in stopwords and word in desc_temp:
        word_split = word.split("-")
        for sub_word in word_split:
            if sub_word in stopwords and word in desc_temp:
                unacceptable_hyphens.add(word)
                desc_temp.remove(word)
                dictionary_questions(sub_word, desc_temp)
            else:
                acceptable_hyphens.add(word)
    if word.__contains__(
            "—") and word not in acceptable_hyphens and word not in unacceptable_hyphens and word not in stopwords and word in desc_temp:
        word_split = word.split("-")
        for sub_word in word_split:
            if sub_word in stopwords and word in desc_temp:
                unacceptable_hyphens.add(word)
                desc_temp.remove(word)
                dictionary_questions(sub_word, desc_temp)
            else:
                acceptable_hyphens.add(word)
    if word.__contains__(
            "—") and word not in acceptable_hyphens and word not in unacceptable_hyphens and word not in stopwords and word in desc_temp:
        word_split = word.split("-")
        for sub_word in word_split:
            if sub_word in stopwords and word in desc_temp:
                unacceptable_hyphens.add(word)
                desc_temp.remove(word)
                dictionary_questions(sub_word, desc_temp)
            else:
                acceptable_hyphens.add(word)
    if word.isupper() and word in desc_temp:
        desc_temp.remove(word)
        desc_temp.append(word.capitalize())
    if word in replacements and word in desc_temp:
        desc_temp.remove(word)
        desc_temp.append(replacements[word])


def one_relations(word_set, location_list, ref_dict, word_comp_table):
    k = 0
    for word1 in word_set:
        print(100 * k / len(word_set))
        k += 1
        for word2 in word_set:
            overlap = 0
            for loc in ref_dict[word2].locations:
                if word1 in location_list[loc]:
                    test_array=numpy.array(location_list[loc])
                    indicies1 = numpy.where(test_array == word1)[0]
                    indicies2 = numpy.where(test_array == word2)[0]
                for index1 in indicies1:
                    for index2 in indicies2:






                    overlap += 1
            if overlap > 0:
                word_comp_table.table[word1][word2] = (len(ref_dict[word1]) / overlap) * ref_dict[
                    word1].weight * ref_dict[word2].weight


def dijkstra(source_word, word_set, word_comp_table):
    distance_to = {}
    graph = {}

    for words in sorted(word_set):
        distance_to[words] = float('inf')
        try:
            graph[words] = word_comp_table.table[source_word][words]
        except KeyError:
            graph[words] = float('inf')
    while graph:
        current_node = min(graph.items(), key=lambda x: x[1])
        if current_node[0] in graph.keys():
            del graph[current_node[0]]

            for neighbor in word_comp_table.table[current_node[0]].keys():
                if distance_to[neighbor] > 1000:
                    test_dist = word_comp_table.table[current_node[0]][neighbor]
                else:
                    test_dist = distance_to[neighbor] + word_comp_table.table[current_node[0]][neighbor]
                if test_dist < distance_to[neighbor]:
                    distance_to[neighbor] = test_dist
                    try:
                        graph[neighbor] = test_dist
                    except KeyError:
                        continue
    for word2 in distance_to.keys():
        word_comp_table.table[source_word][word2] = distance_to[word2]


def word_relations(word_set, location_list, word_comp_table, title_comp_table, book_author_genre):
    k = 0
    for word in word_set:
        print(100 * k / len(word_set))
        k += 1
        dijkstra(word,word_set,word_comp_table)

    avg_length = 0
    for title in location_list:
        avg_length += len(location_list[title])
    avg_length /= len(location_list)
    for title1 in location_list:
        for title2 in location_list:
            total_weight = 0
            for word1 in location_list[title1]:
                for word2 in location_list[title2]:
                    total_weight += word_comp_table.table[word1][word2]
            b = 0.9
            normalized_weight = 1 - b + (b * (len(location_list[title2]) / avg_length))

            title_comp_table.table[title1][title2] = math.floor(
                100000 * total_weight / normalized_weight) / 100000
            if book_author_genre[title1]["description"] == "N/A" or book_author_genre[title2][
                "description"] == "N/A":
                title_comp_table.table[title1][title2] = float('inf')
                print(title1)
                print(title2)

            if title1 == title2:
                title_comp_table.table[title1][title2] = 0

            if book_author_genre[title1]["authors"] != "N/A" and book_author_genre[title2][
                "authors"] != "N/A":
                if type(book_author_genre[title1]["authors"]) is list:
                    for authors1 in book_author_genre[title1]:
                        if type(book_author_genre[title2]["authors"]) is list:
                            for authors2 in book_author_genre[title2]:
                                if authors1 == authors2:
                                    title_comp_table.table[title1][title2] *= .5
                        else:
                            if authors1 == book_author_genre[title2]["authors"]:
                                title_comp_table.table[title1][title2] *= .5
                else:
                    if type(book_author_genre[title2]["authors"]) is list:
                        for authors2 in book_author_genre[title2]:
                            if book_author_genre[title2]["authors"] == authors2:
                                title_comp_table.table[title1][title2] *= .5
                    else:
                        if book_author_genre[title2]["authors"] == book_author_genre[title2][
                            "authors"]:
                            title_comp_table.table[title1][title2] *= .5
            if book_author_genre[title1]["genres"] != "N/A" and book_author_genre[title2][
                "genres"] != "N/A":
                if type(book_author_genre[title1]["genres"]) is list:
                    for genres1 in book_author_genre[title1]:
                        if type(book_author_genre[title2]["genres"]) is list:
                            for genres2 in book_author_genre[title2]:
                                if genres1 == genres2:
                                    title_comp_table.table[title1][title2] *= .9
                        else:
                            if genres1 == book_author_genre[title2]["genres"]:
                                title_comp_table.table[title1][title2] *= .9
                else:
                    if type(book_author_genre[title2]["genres"]) is list:
                        for genres2 in book_author_genre[title2]:
                            if book_author_genre[title2]["genres"] == genres2:
                                title_comp_table.table[title1][title2] *= .9
                    else:
                        if book_author_genre[title2]["genres"] == book_author_genre[title2][
                            "genres"]:
                            title_comp_table.table[title1][title2] *= .9

    for title1 in sorted(title_comp_table.table.keys()):
        print()
        print(title1)
        temp_dict = title_comp_table.table[title1]
        sorted_dict = sorted(temp_dict.items(), key=operator.itemgetter(1))
        for element in sorted_dict:
            print("\t" + str(element[0]) + ": " + str(element[1]))
    title_check = True


dict_final = {}
description_list = []

#Fills the initial descriptions
for items in data["items"]:
    for info in items["volumeInfo"]:
        if info == "description":
            description_list.append(items["volumeInfo"][info])

#Goes through the initial dictionary_questions process
for i in range(0, len(description_list)):
    word_dict = list()
    desc_temp = nltk.word_tokenize(list(description_list)[i])
    for word in desc_temp:
        word_dict.append(word.lower())

    temp_list = word_dict
    for _ in range(0, 4):
        temp_list = word_dict
        for temp_word in temp_list:
            dictionary_questions(temp_word.lower(), word_dict)

    for word in temp_list:
        if word not in stopwords:
            new_word = Word(word.lower())
            dict_final[new_word.name] = new_word

#Creates the list of locations for each word
for items in data["items"]:
    for info in items["volumeInfo"]:
        if type(items["volumeInfo"][info]) is str:
            for test_word in word_tokenize(items["volumeInfo"][info]):
                try:
                    if test_word.lower() in dict_final:
                        dict_final[test_word.lower()].locations.add(items["volumeInfo"]["title"])
                except KeyError:
                    continue
        elif (type(items["volumeInfo"][info]) is list or type(items["volumeInfo"][info]) is tuple) and len(
                items["volumeInfo"][info]) == 1:
            for test_word in word_tokenize(items["volumeInfo"][info][0]):
                try:
                    if test_word.lower() in dict_final:
                        dict_final[test_word.lower()].locations.add(items["volumeInfo"]["title"])
                except KeyError:
                    continue
        elif (type(items["volumeInfo"][info]) is list or type(items["volumeInfo"][info]) is tuple) and len(
                items["volumeInfo"][info]) > 1:
            for i in range(0, len(items["volumeInfo"][info]) - 1):
                for test_word in word_tokenize(items["volumeInfo"][info][i]):
                    try:
                        if test_word.lower() in dict_final:
                            dict_final[test_word.lower()].locations.add(items["volumeInfo"]["title"])
                    except KeyError:
                        continue

temp_list = set()
for keys in sorted(dict_final.keys()):
    temp_list.add(dict_final[keys].share_roots())

dict_final_wordlist = set()
for dict_word in dict_final:
    dict_final_wordlist.add(dict_word)

desc_dict = {}
for items in data["items"]:
    for info in items["volumeInfo"]:
        try:
            desc_dict[items["volumeInfo"]["title"]] = [x.lower() for x in
                                                       word_tokenize(items["volumeInfo"]["description"])]
        except KeyError:
            desc_dict[items["volumeInfo"]["title"]] = "N/A"

#Weights words
for word in dict_final:
    word_weight = 0
    for loc in desc_dict:
        if word in desc_dict[loc]:
            word_weight += 1/(desc_dict[loc].count(word))
    dict_final[word].weight = math.pow(word_weight, 2)

b_a_g = {}
#Fills out bag array
for loc in desc_dict:
    b_a_g[loc] = {}
    for items in data["items"]:
        try:
            b_a_g[loc]["authors"] = items["volumeInfo"]["authors"]
        except KeyError:
            b_a_g[loc]["authors"] = "N/A"
        try:
            b_a_g[loc]["genres"] = items["volumeInfo"]["categories"]
        except KeyError:
            b_a_g[loc]["genres"] = "N/A"
        try:
            b_a_g[loc]["description"] = items["volumeInfo"]["description"]
        except KeyError:
            b_a_g[loc]["description"] = "N/A"

test_dict = {}
test_list = []

for dict_word in sorted(dict_final.keys()):
    test_list.append(dict_final[dict_word])

for i in range(0, len(test_list)):
    test_dict[test_list[i].name] = test_list[i]

#Fills desc_dict with acceptable words in order
for loc in desc_dict:
    if desc_dict[loc] == "N/A":
        continue
    temp_list = [x for x in desc_dict[loc]]
    for test_word in temp_list:
        if (test_word not in dict_final_wordlist and Word(
                test_word).share_roots() not in dict_final_wordlist) or test_word in stopwords:
            while test_word in desc_dict[loc]:
                desc_dict[loc].remove(test_word)
                try:
                    desc_dict[loc].remove(Word(test_word).share_roots())
                except ValueError:
                    continue
        if Word(test_word).share_roots() != test_word and Word(test_word).share_roots() in dict_final_wordlist and Word(
                test_word).share_roots() not in stopwords:
            while test_word in desc_dict[loc]:
                index = desc_dict[loc].index(test_word)
                desc_dict[loc][index] = Word(test_word).share_roots()
                try:
                    desc_dict[loc].remove(Word(test_word).share_roots())
                except ValueError:
                    continue
        if test_word not in dict_final_wordlist and test_word in desc_dict[loc]:
            while test_word in desc_dict[loc]:
                desc_dict[loc].remove(test_word)
                try:
                    desc_dict[loc].remove(Word(test_word).share_roots())
                except ValueError:
                    continue

for loc in desc_dict:
    print(loc)
    print("\t" + str(desc_dict[loc]))

word_set = set(test_dict.keys())
title_comp_table = Comp_Table(sorted(desc_dict))
word_comp_table = Comp_Table(sorted(test_dict))

one_relations(word_set, desc_dict, test_dict, word_comp_table)
word_relations(word_set, desc_dict, word_comp_table, title_comp_table, b_a_g)

# for word in sorted(dict_final_wordlist):
#     print(word)

# for word in sorted(stopwords):
#     print(word)


# map = Relationship_Map(test_dict, desc_dict, b_a_g)
# map.draw_map()
# map_comp_table = map.title_comp_table

# with open('Text_Pickles/wordMap.pkl', 'rb') as handle:
#     map_comp_table = pickle.load(handle)
# print(map_comp_table)

with open('Text_Pickles/stopwords.pkl', 'wb') as rehandle6:
    pickle.dump(stopwords, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
with open('Text_Pickles/AcceptableHyphens.pkl', 'wb') as rehandle6:
    pickle.dump(acceptable_hyphens, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
with open('Text_Pickles/UnacceptableHyphens.pkl', 'wb') as rehandle6:
    pickle.dump(unacceptable_hyphens, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
with open('Text_Pickles/Replacements.pkl', 'wb') as rehandle6:
    pickle.dump(replacements, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
with open('Text_Pickles/Irreplacements.pkl', 'wb') as rehandle6:
    pickle.dump(irreplacements, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
# with open('Book_Pickles/DictFinal.pkl', 'wb') as rehandle6:
#     pickle.dump(dict_final, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
with open('Book_Pickles/JSONDict.pkl', 'wb') as rehandle6:
    pickle.dump(dict_final, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
# with open('Text_Pickles/wordMap.pkl', 'wb') as rehandle6:
#     pickle.dump(map_comp_table, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
# with open('Book_Pickles/DictDict.pkl', 'wb') as rehandle6:
#     pickle.dump(dict_final, rehandle6, protocol=pickle.HIGHEST_PROTOCOL)
