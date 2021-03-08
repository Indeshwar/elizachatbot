#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Eliza homework: it is a hard coded chatbot homework that can reconize human feeling and relation and some past verb 
"""

"""
Created on Sat Feb  6 02:49:18 2021

author_ = indeshwarchaudhary
"""

import re
import random
# data = [{"pattern":["I am happy today", "I am so excited", "Today! I'm in joyful mood" ],
#         "Responses": ["Nice", "I am glad that you are happy"]}]

data = {"intent":[{"tag":"None",
                "pattern":["abc"],
                "resopose":["Tell me more"]},
                {"tag":"happy",
                "pattern":["happy","excited", "joyful", "good","ok","fine","well"],
                "resopose":["Good! tell me more", "Nice! tell me more"]},
               {"tag": "sad",
                "pattern":["sad", "painfull","sadness"],
                "resopose":["Sorry to hear that", "I'm sorry"]},
               {"tag":"father",
                   "pattern": ["father","dad","papa","dad's","papa's","father's","dady", "dady's"],
                "resopose":["What does your father do?", "Does your father like any sport?"]},
               {"tag":"brother",
                   "pattern": ["brother","brothers","brother's"],
                "resopose":["How many brother do you have?", "Does your brother love you?"]},
               {"tag":"mom",
                   "pattern": ["mother", "mom","mommy","mom's","mother's","momy's"],
                "resopose":["What does your mother like to cook?", "Does your mother like any sport?"]},
               {"tag":"sister",
                   "pattern": ["sister","sister","sister's"],
                "resopose":["What does your sister like to cook?", "Is she younger than you?"]},
               {"tag":"friend",
                   "pattern": ["friend", "friends","friend's"],
                "resopose":["how did you meet your friend?", "where did you meet your friend?"]},
               {"tag": "past",
                "pattern":['ed'],
                "resopose":["why did ","How did "]},
               {"tag": "name",
                "pattern":["name", "I am"],
                "resopose":["hello","Hi"]},
               {"tag":"greeting",
                "pattern":["hi", "hello"],
                "resopose":["Hi","Hello"]}
               ]}


def predict_tag(wrds, pattern, tag):
    count = 0
    listB = []
    for w in wrds:
        if w in pattern:
            #count the number words that matches in the pattern list
            count = count+1
            
        elif re.findall('ed', w):
            if 'ed' in pattern:
                count = count + 1
                
    #find the probality of number of matches words over lenght of pattern
    p = count/len(pattern)
    
    #insert 'p' and and 'tag' in listB
    listB.append(p)
    listB.append(tag)
    
    #convert listB into tuple
    tupleA = tuple(listB)
    return tupleA


def tag_return(txt):
    listD = []
    for intends in data['intent']:
        for patern in intends['pattern']:
            #split the pattern 
            wrds = patern.split()
            #tag 
            tg = intends['tag']
            #return the probality of corresponding tag as tuple
            tupleC = predict_tag(txt, wrds, tg)
            #insert the tuple in listD
            listD.append(tupleC)
    
    return listD

def find_tag_of_max_p(listD):
    max = -1
    tag = ""
    for tpl in listD:
        pb, tg = tpl
        if max < pb:
            max = pb
            tag = tg
    return tag

def analyze_anwer(tg, v):
    
    for t in data['intent']:
        if t['tag'] == tg:
            
            #create a list of all responses
            y = [x for x in t['resopose']]
            if t['tag'] == 'past':
                
                for w in v:
                    if re.findall('ed', w):
                        d = w
                        if re.sub('ed',' ', d):
                            #remove 'ed' from d 
                            #then v_1 holds present verb
                            v_1 = re.sub('ed',' ', d)
                            break
                
                if re.findall(r'[she|he]', v[0]):
                    #s holds the subject of sentence
                    s = v[0]
                elif re.findall(r'[i]',v[0]):
                    s = 'you'
                elif re.findall(r'[you]', v[0]):
                    s = "I"
                
                #randomonly pick response from list y and print it
                print(y[random.randint(0,(len(y)-1))],s,v_1,"?")
                break
            elif t['tag'] == 'name':
                print(y[random.randint(0,(len(y)-1))], v[(len(v)-1)])
                break
            else:
                print(y[random.randint(0,(len(y)-1))])
                break
            
def chatting():
    print("What is your name ?")
    while True:
        inp = input("You: ")
        inp = inp.lower()
        if inp == "bye":
            print("Bye!","\n Seee you!")
            break
        else:
            #split the input sentence into words of list
            t = inp.split()
            #return all the tags
            listC = tag_return(t)
            #return the  appropriate tag 
            tgs = find_tag_of_max_p(listC)
            #analyze the input words and respnse back to user
            analyze_anwer(tgs,t)
           
    
chatting()