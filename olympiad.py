# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:54:31 2024

@author: omidg
"""
j = 0
l = 0
final = []
ff = []
mm = []
a = int(input())
for i in range(0,a):
    file = input()
    q = file.split('.')
    final.append(q)

for i in range(a):
    final[i][1]=final[i][1].capitalize()
for words in final:
    if words[j][0] == 'f':
        ff.append(words)
    else:
        mm.append(words)
#for words in ff:
#    print(words[0],words)
ff=sorted(ff, key=lambda student: student[1]) 
mm=sorted(mm, key=lambda student: student[1]) 
for i in range(len(ff)):
        print(ff[i][0],ff[i][1],ff[i][2])

for j in range(len(mm)):
        print(mm[j][0],mm[j][1],mm[j][2])