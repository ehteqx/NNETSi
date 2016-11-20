#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

wordlist = list()
wordcount = list()
probability = list()
entropy = 0.0

with open('file.txt', 'r') as text:
    for line in text:
        for word in line.split():
            if word in wordlist:
                wordcount[wordlist.index(word)] = wordcount[wordlist.index(word)] + 1
            else:
                wordlist.append(word)
                wordcount.append(1)

textlenght = sum(wordcount)
wordsnr = len(wordlist)
for step1 in wordcount:
    probability.append(step1/textlenght)
for step2 in probability:
    entropy = entropy + (step2 * math.log((1.0 / step2), 2))
entpw = entropy/textlenght


print("Total word entropy: ")
print(entropy)
print(" ")
print("Entropy per written word:")
print(entpw)
print(" ")
