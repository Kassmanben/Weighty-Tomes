import pickle

f=open("Text_Reference/small.txt",'r')
# g=open("/Text_Reference/actor-givenname",'r')
# h=open("/Text_Reference/actor-surname",'r')
# i=open("/Text_Reference/actor-givenname",'r')
# j=open("/Text_Reference/ASSurnames",'r')
# k=open("/Text_Reference/Family-Names",'r')
# l=open("/Text_Reference/Given-Names",'r')
temp_list=f.readlines()
# for element in g.readlines():
#     dictionarylist.append(element.capitalize())
# for element in h.readlines():
#     dictionarylist.append(element.capitalize())
# for element in i.readlines():
#     dictionarylist.append(element.capitalize())
# for element in j.readlines():
#     dictionarylist.append(element.capitalize())
# for element in k.readlines():
#     dictionarylist.append(element.capitalize())
# for element in l.readlines():
#     dictionarylist.append(element.capitalize())
dictionarylist=set()
for line in temp_list:
    line=line.strip()
    dictionarylist.add(line)

for word in dictionarylist:
    print(word)

dictionarylist=set(dictionarylist)

with open('Text_Pickles/Dictionary.pkl', 'wb') as rehandle:
    pickle.dump(dictionarylist, rehandle, protocol=pickle.HIGHEST_PROTOCOL)