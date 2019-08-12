#!/usr/bin/python
# -*- coding: UTF-8 -*
import  re
import os

#os.mkdir("file")
f_r = open("slice/new_slices_1.txt")
index=1
line = f_r.readline()
f_w=open("error.txt","a+")

while line:
    
    if "/home/zhaoxuanchen" in line:
        path=line.split(' ')[1]
        #print path
        f_w.write("}")
        f_w = open("compcode/function_%d.c" % index, "a+")
        print index 
        num=0
        f_w.write("int function_%d(){" % index)
        f_w.write("\n")
        index = index + 1
        line=f_r.readline()
        line=f_r.readline()
    if line.startswith("-----------"):
        line=f_r.readline()  
        continue
    
    #print line
    line_num=line.split(' ')[-1]
    #print line_num
    if line_num==';\n':
        line_num='100000'
    if line.find(";")==-1:
       if line.find("if")==-1:
           if line.find("for")==-1:
               if line.find("while")==-1:
                  if line.find("else")==-1:
                      line=f_r.readline()
                      continue
           
    #print line_num
    line=' '.join(line.split(" ")[:-1])
    if line.find("\n") == -1:
        line=line+"\n"
    #line=line+"\n"
    #line= "".join( line.split(" ")[:-1])
    if int(line_num)<num or int(line_num)==num:
        line=f_r.readline()
        continue 
    if line.startswith("if"):
        #print line
        f_source=open(path)
        #print(line_num)
        line_source = f_source.readlines()
        flag=0
        for i in range(int(line_num),len(line_source)):
            #print (line_source[i])
            if '/*' in line_source[i]:
                continue
            if '*/' in line_source[i]:
                continue
            if '#' in line_source[i]:
                continue
            line=line+line_source[i]
            if "{" in line_source[i]:
                flag=flag+1
            #print line
            if '}' in line_source[i]:
               flag=flag-1
               if flag==0:
                    num=i
                    break
    if line.startswith("for"):
        #print line
        f_source=open(path)
        #print(line_num)
        line_source = f_source.readlines()
        flag=0
        for i in range(int(line_num),len(line_source)):
            #print (line_source[i])
            if '/*' in line_source[i]:
                continue
            if '*/' in line_source[i]:
                continue
            if '#' in line_source[i]:
                continue
            line=line+line_source[i]
            if "{" in line_source[i]:
                flag=flag+1
            #print line
            if '}' in line_source[i]:
               flag=flag-1
               if flag==0:
                    num=i
                    break
    if line.startswith("while"):
        #print line
        f_source=open(path)
        #print(line_num)
        line_source = f_source.readlines()
        flag=0
        if int(line_num)==len(line_source):
             line=f_r.readline()
             continue
        if int(line_num)>len(line_source):
             line=f_r.readline()
             continue
        if line_source[int(line_num)].find("{")==-1:
            line=line
        else:
            print 'while'
            for i in range(int(line_num),len(line_source)):
                #print (line_source[i])
                if '/*' in line_source[i]:
                    continue
                if '*/' in line_source[i]:
                    continue
                if '#' in line_source[i]:
                    continue
                line=line+line_source[i]
                if "{" in line_source[i]:
                    flag=flag+1
                #print line
                if '}' in line_source[i]:
                   flag=flag-1
                   if flag==0:
                        num=i
                        break
    if line.startswith("else"):
        #print line
        f_source=open(path)
        #print(line_num)
        line_source = f_source.readlines()
        flag=0
        for i in range(int(line_num),len(line_source)):
            #print (line_source[i])
            if '/*' in line_source[i]:
                continue
            if '*/' in line_source[i]:
                continue
            if '#' in line_source[i]:
                continue
            line=line+line_source[i]
            if "{" in line_source[i]:
                flag=flag+1
            #print line
            if '}' in line_source[i]:
               flag=flag-1
               if flag==0:
                    num=i
                    break
    if line.find("/home/zhaoxuanchen/tangjing") == -1:
        #print "write"
        #print line
        f_w.write(line)
    line=f_r.readline()
f_w.write("}")
f_r.close()
print "END"


