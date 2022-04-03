from gp import MorphologicalAnalysis
import re
import csv

f = open("word.txt", "r")
words=[]
roots=[]
pre=[]
suf=[]
stemmer=MorphologicalAnalysis()
for line in f.read().split():
    word=line.split('\'')
    #print(word[1])
    root,prefix,suffix=stemmer.get_root(word[1])
    print("word: ", word[1])
    print("root: ", root)
    print("prefix: ", prefix)
    print("suffix: ", suffix)
    print('-------------------------------------')
    if root not in roots and len(root) !=0:
        roots.append(root)
    if prefix not in pre and len(prefix)!=0:
        pre.append(prefix)
    if suffix not in suf and len(suffix) !=0:
        suf.append(suffix)
data_words=roots+pre+suf
data_set=[]
for i in range(len(data_words)):
    data_set.append([data_words[i]])
print(len(data_set))
with open('LabelsCSV.csv', 'w', newline='',encoding='utf-8') as x:
    writer = csv.writer(x)
    for i in data_set:
        writer.writerow(i)