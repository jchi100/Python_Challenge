# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:28:08 2018

@author: Jing

PyParagraph 
"""

import re

import os


fileName = os.path.join('..', 'PyParagraph', 'paragraph_1.txt')


with open(fileName, 'r') as file:
    
    paragraph= file.read()
    sentences =re.split(r' *[\.\?!][\'"\)\]]* +', paragraph)
   
    totalWord= 0

    for sentence in sentences:
        count = len(re.findall("[a-zA-Z_]+", sentence))
        totalWord = totalWord+count 
        print(sentence+"\n")
  
    print('Total word count:   ', len(paragraph.split()))
    print('Sentence count:    ', len(sentences))
 
    print("Average sentence length: ", totalWord/len(sentences))