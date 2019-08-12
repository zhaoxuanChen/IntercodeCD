#!/usr/bin/python
# -*- coding: UTF-8 -*
import sys
sys.setrecursionlimit(1000000)
parent_list=[]      #父节点列表
map_list=[]         #父节点与子节点一一对应列表
node_list = []      #节点列表
node_flag=[]


def Creatlistfor_parent(node):              #为父节点创建列表
    flag_parent = 0
    for i in range(len(parent_list)):
         if node==parent_list[i]:
                flag_parent=1
    if flag_parent==0:
        #print node
        parent_list.append(node)
        map_list.append([])

def Addchildto_parent_list(node_p,node_s):   #将孩子节点加到对应的父节点列表
    for i in range(len(parent_list)):
         if node_p==parent_list[i]:
                 map_list[i].append(node_s)

def Findparent_index(s):                    #为子节点找到对应父节点的索引
    num=-1
    for i in map_list:
        if s in i:
            num= map_list.index(i)
    return num

def is_parentnode(panduan):                 #判断一个节点是父节点还是叶子节点
    panduan_index=-1
    for i in parent_list:
        if panduan==i:
            panduan_index=parent_list.index(i)
    return panduan_index

def findchild(node,list_seq):
    p_num=is_parentnode(node) 
    #print node
    #print p_num #父节点下标
    if p_num==-1:
        return
    child=map_list[p_num]
    #print(len(child))
    #print len(child)
    #print len(list_seq)
    for i in range(len(child)):
        #print(len(child))
        list_seq.append(child[i])
        #print child[i]
        findchild(child[i],list_seq)


def DFS(f,path):
    f1=open(path)
    line=f1.readline()
    root=''
    list_seq=[]
    while line :
        if 'FunctionDef' in line:
            #print line
            root=line.split(" {childNum")[0].split("n")[1]
            break
        line=f1.readline()
    f1.close() 
    #print root
    list_seq.append(root)
    #print(parent_list)
    #print(len(map_list))
    #print(len(node_list))
    findchild(root,list_seq)
    #print(len(list_seq))
  
    f1=open(path)
    lines=f1.readlines()
    for i in list_seq:
        print i
        for j in lines:
            id=j.split(" {childNum")[0].split("n")[1]
            #print id
            if i==id: 
                node_c = j.split(",functionId")[0].split("code:")[1][1:-1]
                #node_t = j.split("type:")[1][1:-4]
                
                f.write(node_c+" ")
    
    

def Data_preprocess(f,f_new,path):    #数据预处理

    line = f.readline()
    count = 1
    while line:
        #print count
        flag_node_p = 0
        flag_node_s =0 
        #print line
        node_p = line.split("--")[0].strip()
        node_s = line.split("--")[1].replace('\n','').replace(';','').strip()
        
        #print node_p
        #print node_s
        Creatlistfor_parent(node_p)     #生成父节点列表
        for i in range(len(node_list)):
            if node_p==node_list[i]:
                flag_node_p=1
            if node_s==node_list[i]:
                flag_node_s=1
        if flag_node_p==0:
            node_list.append(node_p)
            #print("add")
            node_flag.append("0")
        if flag_node_s==0:
            node_list.append(node_s)
        #print("add")
        node_flag.append("0")
        Addchildto_parent_list(node_p,node_s)  #print  #把孩子节点加入到父节点列表中
        #Embedding 孩子节点
        line = f.readline()
        count=count+1
    #print('do dfs')
    DFS(f_new,path) #深度优先遍历
    '''
    for i in range(len(parent_list)):
        f_new.write(parent_list[i]+'-----')
        for j in range(len(map_list[i])):
            f_new.write(map_list[i][j]+'     ')
        f_new.write('\n')
    '''
if __name__ == '__main__':
    for i in range(1,10001):
        print i
        parent_list = []  # 父节点列表
        map_list = []  # 父节点与子节点一一对应列表
        node_list = []  # 节点列表
        node_flag = []
        f = open("link_file/function_" + str(i) + ".txt")
        f_new=open("DFS_sequence/function_" + str(i) + ".txt", "a+")
        path="node_file/function_"+str(i) + ".txt"
        Data_preprocess(f,f_new,path)
        f.close()
        #h = SubstreeLayer(node_list, parent_list, map_list,i)
        f_new.close()


   # while line:
        #code = ""
        #type = ""
        #for i in line.split(" "):
          #  code=code+i.split("#")[0]+" "
           # type=type+i.split("#")[1]+" "
        #f_code.write(code+"\n")
       # f_type.write(type)
        #line=f_x.readline()




