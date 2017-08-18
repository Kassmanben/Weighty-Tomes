import pickle
import re
import string

with open('SampleDict.pkl', 'rb') as handle:
    bookDict = pickle.load(handle)
with open('Dictionary.pkl', 'rb') as handle:
    dictionary = pickle.load(handle)
with open('NameDict.pkl', 'rb') as handle:
    name = pickle.load(handle)
with open('RefinedList.pkl', 'rb') as handle:
    wordlist = pickle.load(handle)
exclude = set(string.punctuation)
exclude.add("’")
exclude.add("…")
exclude.add("”")
exclude.add("“")

def endsinpunct(word):
    for i in range(0, 3):
        for punct in exclude:
            if word.endswith(punct):
                word = word[0:len(word) - 1]
    return word


def beginsinpunct(word):
    for i in range(0, 10):
        for punct in exclude:
            if word.startswith(punct):
                word = word[1:len(word)]
    return word


def reevaluate():
    tempstring = ''
    for i in range(1, len(bookDict)):
        tempstring += str(bookDict[i]['Title']) + " " + str(
            bookDict[i]['Description']) + " " + ''.join(str(p) + " " for p in bookDict[i]['Genre'])
        if tempstring.__contains__("—"):
            tempstring = tempstring.replace("—", "-")
        if tempstring.__contains__("--"):
            tempstring = tempstring.replace("--", "-")
        if tempstring.__contains__("’"):
            tempstring = tempstring.replace("’", "'")
    tempstring = tempstring.split()
    tempstring = set(tempstring)
    newwordlist = wordlist
    for tempword in tempstring:
        if tempword in newwordlist:
            continue
        for punct in exclude:
            if tempword.endswith(punct):
                tempword = endsinpunct(tempword)
            if tempword.endswith(str(punct) + "s"):
                tempword = tempword[0:len(tempword) - 2]
            if tempword.startswith(punct):
                tempword = beginsinpunct(tempword)
            if tempword.isdecimal():
                tempword = "the"
        if tempword.__contains__("-") and tempword.lower() not in dictionary:
            gwords = 0
            # print(tempword)
            for element in tempword.split("-"):
                # print(element)
                if element.lower() in dictionary:
                    gwords += 1
            if gwords == len(tempword.split()):
                for element in tempword.split("-"):
                    newwordlist.add(element)
                    # print("yep")
                continue
            if gwords > 0:
                print(tempword)
                f = input("Is this a word?")
                if f == "y" or f == "Y":
                    newwordlist.add(tempword)
                    dictionary.add(tempword.lower())
                    continue
                else:
                    for element in tempword.split("-"):
                        newwordlist.add(element)

                    continue
        newwordlist.add(tempword)
        return newwordlist


tempset = set("the")
for word in wordlist:
    if len(word) == 1 and word.lower() != "a" and word.lower() != "i":
        continue
    if word in name:
        continue
    # if word.isupper() and not word.istitle():
    #     print(word)
    #     f=input("Name?")
    #     if f=="y":
    #         tempset.add(word)
    #     elif f=="t":
    #         tempset.add(word.capitalize)
    #     elif f=="d":
    #         continue
    #     else:
    #         tempset.add(word.lower())

    if str(word.lower()) not in dictionary and str(word) not in name:
        print(word)
        for punct in exclude:
            if word.__contains__(punct):
                print(word.split(punct))
                f = input("Good split?")
                if f == "y":
                    word = "the"
                    for element in word.split(punct):
                        tempset.add(element)
        continue
    tempset.add(word)
for element in sorted(tempset):
    print(element)
for element in sorted(name):
    print(element)

with open('Dictionary.pkl', 'wb') as rehandle:
    pickle.dump(dictionary, rehandle, protocol=pickle.HIGHEST_PROTOCOL)
with open('NameDict.pkl', 'wb') as rehandle:
    pickle.dump(name, rehandle, protocol=pickle.HIGHEST_PROTOCOL)
with open('RefinedList.pkl', 'wb') as rehandle:
    pickle.dump(tempset, rehandle, protocol=pickle.HIGHEST_PROTOCOL)
