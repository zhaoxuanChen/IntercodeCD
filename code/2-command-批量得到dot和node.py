#!/usr/bin/python
# -*- coding: UTF-8 -*
from igraph import *
from joern.all import JoernSteps
import os
import pickle
from py2neo.packages.httpstream import http
http.socket_timeout = 99999

def getFuncId(db, func_name):
    query_str = 'getFunctionsByName("' + func_name + '").id'
    func_id = db.runGremlinQuery(query_str)
    #print func_id
    return func_id[0]
    


if __name__ == '__main__':
    '''
    j = JoernSteps()
    j.setGraphDbURL('http://localhost:7474/db/data/')
# j.addStepsDir('Use this to inject utility traversals')
    j.connectToDatabase()
    index=1
    listid=[]
    #f=open("funcid_1000.pkl","a+")
    
    for i in range(1,10001):
        print i
        func_name="function_%d" %i
        func_id=getFuncId(j, func_name)
        listid.append(func_id)
    f=open('id.pkl','wb')
    pickle.dump(listid,f)
    
    
    f=open('id.pkl','rb')
    listid=pickle.load(f)
    print(len(listid))
    #j=5001
    
    path=os.getcwd()
    os.chdir("../../neo4j/bin/")
    os.system('./neo4j restart')
    os.chdir(path)
    
    for i in range(5000,len(listid)):
        command="echo 'queryNodeIndex(\"functionId:"+str(listid[i])+"\")' | joern-lookup -g > node_file/function_"+str(j)+".txt" 
        os.system(command)
        print j
        j=j+1
   
      
    j=9371
    for i in range(0,3000):
        command="echo 'getFunctionsByName(\"function_"+str(j)+"\").id' | joern-lookup -g | tail -n 1 | joern-plot-ast > dot_file/function_"+str(j)+".txt" 
        os.system(command)
        print j
        j=j+1
    '''    
    for i in range(1,10001):
        print i
        f = open("dot_file/function_" + str(i) + ".txt")
        f_new=open("link_file/function_" + str(i) + ".txt", "a+")
        line=f.readline()
        while line:
            if ' -- ' in line:
                f_new.write(line)
            line=f.readline()
        f.close()
        f_new.close()
