#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:16:21 2021

@author: kulinducooray
"""

def found(file2, words, keyboard):
    list1 = []
    for i in open(file2): #puts the incorrectly spelt words in a list
        i = i.strip().split()
        list1.append(i)

    for a in list1:
        strin = "".join(a)
        if strin in words:
            length = len(strin)
            print(" "*(15-length) + strin + " -> FOUND")
        else:
            possible = set() #creating a set of possible strings
            
            for i in range(len(strin)): #drop a character
                string_temp = strin
                l = list(string_temp)
                l.pop(i)
                string_temp = ''.join(l)
                if string_temp in words: #checks the dictionary of words and adds it the set if there is a match
                    possible.add(string_temp)

            for j in range(len(strin)+1): #insert a character
                for letter in keyboard:
                    string_temp = strin
                    list3 = list(string_temp)
                    list3.insert(j, letter)
                    string_temp = ''.join(list3)
                    if string_temp in words:
                        possible.add(string_temp)

            for k in range(len(strin)-1): #swap a character
                string_temp = strin
                list2 = list(string_temp)
                temp = list2[k]
                list2[k] = list2[k+1]
                list2[k+1] = temp
                string_temp = ''.join(list2)
                if string_temp in words:
                    possible.add(string_temp)

            for m in range(len(strin)): #replace a character
                for n in keyboard[strin[m]]:
                    string_temp = strin
                    l = list(string_temp)
                    l[m] = str(n)
                    string_temp = ''.join(l)
                    if string_temp in words:
                        possible.add(string_temp)
                    
                       
            if (len(possible) != 0):
                list_vals = []
                for i in possible:
                    list_vals.append((words[i],i))
                list_vals.sort(reverse=True) #appends all possible words to a list and orders them in reverse order
                word_list = []
                if (len(possible) > 3):
                    for i in range(3):
                        word_list.append(list_vals[i][1])
                else:
                    for j in range(len(possible)):
                        word_list.append(list_vals[j][1])
                length = len(strin)
                if (len(possible) < 10): #prints the list of possible words 
                    print(" "*(15-length) + strin + " -> FOUND  {}:  ".format(len(possible)),end="")
                    print(*word_list)
                else:
                    print(" "*(15-length) + strin + " -> FOUND {}:  ".format(len(possible)),end="")
                    print(*word_list)

            else: #couldnt find an autocorrected word
                length = len(strin)
                print(" "*(15-length) + strin + " -> NOT FOUND")


if __name__ == "__main__":
    file1 = input("Dictionary file => ").strip()
    print(file1)
    file2 = input("Input file => ").strip()
    print(file2)
    file3 = input("Keyboard file => ").strip()
    print(file3)

    words = dict() #creates a dictionary of all the available words
    for line in open(file1):
        line = line.strip().split(',')
        word = line[0].strip()
        frequency = line[1].strip()

        if word not in words: #uses word as key and adds its second value
            words[word] = frequency

    keyboard = dict()
    for line1 in open(file3): # sets up the keyboard dictionary
        line1 = line1.strip().split()
        starting = line1[0]
        rest = line1[1::]
        if starting not in keyboard:
            keyboard[starting] = rest

    found(file2,words,keyboard) #calls found to return the correctly spelt word
