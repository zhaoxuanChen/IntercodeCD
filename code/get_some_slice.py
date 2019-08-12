#!/usr/bin/python
# -*- coding: UTF-8 -*
import  re
import os

#os.mkdir("file")

def func(listtemp,n):
    for i in range(0,len(listtemp),n):
       yield listtemp[i:i+n]

if __name__ == '__main__':
    f_r = open("api_slices.txt")
    slices=f_r.read().split("------------------------------")
    print len(slices)
    list_split=func(slices,10000)
    k=1
    for i in list_split:
        f_w=open("slice/new_slices_"+str(k)+".txt","a+")
        for j in i:
            f_w.write(j+"------------------------------")
        k=k+1    
    f_r.close()


