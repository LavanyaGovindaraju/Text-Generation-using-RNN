# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:43:53 2021

@author: akash
"""
import os
from typing import List, Dict
import numpy as np
import operator
from collections import Counter
import re

def preprocess_english(text) -> List:
    
    text = os.linesep.join([s for s in text.splitlines() if s])
    text= text.lower().split('.')
    text = [i for i in text if i]
    clean_data=[]
    whitespace = re.compile(u"[\s\u0020\u00a0\u1680\u180e\u202f\u205f\u3000\u2000-\u200a]+", re.UNICODE)
    punctSeq   = u"['\"“”‘’]+|[.?!,…]+|[:;]+"
    punc = u"[(),$%^&#*_+={}\[\]:\"|\'\~`<>/,¦!?½£¶¼©⅐⅑⅒⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟↉¤¿º;-]+"
    for i in text:
        t1= whitespace.sub(" ",i).strip()
        t1 = re.sub(punctSeq, "", t1)
        t1 = re.sub(punc, " ", t1)
        final = re.sub(r'[0-9]+', "" , t1)
        clean_data.append(final)
    return clean_data
    

def preprocess_bengali(text) -> List:
    
    text = os.linesep.join([s for s in text.splitlines() if s])
    bengali_fullstop= u"\u0964"
    text= text.split(bengali_fullstop)
    text = [i for i in text if i]
    clean_data=[]
    whitespace = re.compile(u"[\s\u0020\u00a0\u1680\u180e\u202f\u205f\u3000\u2000-\u200a]+", re.UNICODE)
    punctSeq   = u"['\"“”‘’]+|[.?!,…]+|[:;]+"
    punc = u"[(),$%^&#*_+={}\[\]:\"|\'\~`<>/,¦!?½£¶¼©⅐⅑⅒⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟↉¤¿º;-]+"
    for i in text:
        t1= whitespace.sub(" ",i).strip()
        t1 = re.sub(punctSeq, "", t1)
        t1 = re.sub(punc, "", t1)
        t1 = re.sub(r'[0-9]+', "" , t1)
        final = re.sub(r'[A-Za-z]+', "" , t1)
        clean_data.append(final)

    return clean_data
   
def train_test_split_data(text:List, test_size:float=0.2):
    
    train=[]
    test= []
    
    j=-1
    for i in range(int(len(text)*(1-test_size))):
        train.append(text[i])
        j=j+1
        
    for i in range(int(len(text)*test_size)):
        j=j+1
        test.append(text[j])
    
    return train, test

        

