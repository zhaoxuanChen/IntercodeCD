#!/usr/bin/python
# -*- coding: UTF-8 -*
import  re
import os

#os.mkdir("file")
f_r = open("slice/new_slices_1.txt")
slices=f_r.read().split("------------------------------")
print len(slices)
for i in range(1,10001):
    print i
    f_comp=open("compcode/function_" + str(i) + ".c")
    data=f_comp.read().split("\n")
    #print data
    line=''
    slice=slices[i-1].split("\n")
    for k in data:
        k_1= k.strip().replace(" ",'')
        #y=list(k.strip().replace("\t",""))
        #k_1="".join(y)
        
        #print k.replace(" ",'')+"______"
        flag=0
        for j in slice:
           x=" ".join(j.split(" ")[0:-1]).replace(" ",'')
           #print x
           if k_1==x:
                flag=1
           if '}' in k:
              flag=1
           if "{" in k:
              flag=1
           if 'int function_' in k:
              flag=1
        if flag==1:
           line=line+"\n"+k
    #print line
    f1=open("final_comp/function_"+str(i)+".c","a+")
    f1.write(line)


