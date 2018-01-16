#Import web data and do word count

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0)+1

word_count = []
for k,y in counts.items():
    new_tuple = (y,k)
    word_count.append(new_tuple)

word_count = sorted(word_count,reverse=True)

for key,value in word_count:
    print(value,key)
