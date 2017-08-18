file="bookIdentifier.txt"

f = open(file, 'r')

list = []
for line in f:
    list.append(line.replace("\n", ""))
print(list)
g = open(file, 'w')

i = 0
for line in list:
    flag=0
    j = 0
    for line2 in list:
        if list[i] == list[j] and i != j:
            flag=1
        j += 1
    if flag == 0:
        g.write(str(list[i]) + "\n")
    list[i]="\0"
    i += 1
g.close()
f.close()
