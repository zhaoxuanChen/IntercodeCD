## coding:utf-8

import os
import re
import pickle
from get_tokens import create_tokens
from mapping import *

def make_corpus():
    corpus=[]
    dl_corpus=[]
    for i in range(1,10001): 
        print i
        f=open("DFS_sequence/function_" + str(i) + ".txt")
        s = f.read()
        f.close()
        words = []
        #get token
        words = create_tokens(s)
        #print(words)
        #get map
        m=[]
        m.append(words)
        k=mapping(m)
        k="".join(k)
        mapwords=k.split(' ')
        
        f1 = open("map_sequence/function_" + str(i) + ".txt","a+")
        for i in mapwords :
           f1.write(i.strip()+" ")
        f1.close()
        corpus=corpus+mapwords
        
    f2=open("corpus.pkl","a+")
    dl_corpus.append(corpus)
    pickle.dump(dl_corpus,f2)
    #for j in corpus:
    #    f2.write(j.strip()+" ") 
make_corpus()
