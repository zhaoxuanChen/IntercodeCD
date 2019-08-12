## coding:utf-8
import re
import os
import string
#import xlrd


def isphor(s, liter):
    m = re.search(liter,s)
    if m is not None:
        return True
    else: 
        return False

    
def doubisphor(forward, back):
    double = ('->','--','-=','+=','++','>=','<=','==','!=','*=','/=','%=','/=','&=','^=','||','&&','>>','<<')
    string=forward+back
    
    if string in double:
        return True
    else:  
        return False

    
def trisphor(s,t):
    if (s=='>>')|(s=='<<')and(t=='='):
        return True
    else:
        return False
    

def create_tokens(sentence):
    #print "creat_tokens"
    formal='^[_a-zA-Z][_a-zA-Z0-9]*$'
    phla='[^_a-zA-Z0-9]'
    space='\s'
    spa=''
    string=[]
    j=0
    str = sentence
    i=0
    #print len(str) 
    while(i<len(str)):
        if isphor(str[i],space):
            if i>j:
                string.append(str[j:i])
                j=i+1 
            else:
                j=i+1
                
        elif isphor(str[i],phla):    
            if (i+1<len(str))and isphor(str[i+1],phla):
                m=doubisphor(str[i],str[i+1])
                
                if m:
                    string1=str[i]+str[i+1]
                    
                    if (i+2<len(str))and (isphor(str[i+2],phla)):
                        if trisphor(string1,str[i+2]):
                            string.append(str[j:i])
                            string.append(str[i]+str[i+1]+str[i+2])
                            j=i+3
                            i=i+2
                            
                        else:
                            string.append(str[j:i])
                            string.append(str[i]+str[i+1])
                            string.append(str[i+2])
                            j=i+3
                            i=i+2
                            
                    else:
                        string.append(str[j:i])
                        string.append(str[i]+str[i+1])
                        j=i+2
                        i=i+1
                        
                else:
                    string.append(str[j:i])
                    string.append(str[i])
                    string.append(str[i+1])
                    j=i+2
                    i=i+1
                    
            else:
                string.append(str[j:i])
                string.append(str[i])
                j=i+1
                
        i=i+1
        #print i
        
    count=0
    count1=0
    sub0='\r'
    
    if sub0 in string:
        string.remove('\r')
        
    for sub1 in string:
        if sub1==' ':
            count1=count1+1
            
    for j in range(count1):
        string.remove(' ')
        
    for sub in string:
        if sub==spa:
            count=count+1
            
    for i in range(count):
        string.remove('')
        
    return string




# Add this function for process code files in this folder to make the vocabulary
def make_vocabulary():
	#scan each folder
	for root,dirs,files in os.walk(os.path.abspath('CWE-1000')):
		#print(root)
		#print(files)
		for codefile in files:
			#read each file
			f = open(root+"\\"+codefile,"r")
			code = f.read()
			f.close()

			#delete the notes in the code
			#Note_Rule = "(\/\*(\s|.)*?\*\/)|(\/\/.*\s)"
			#code = re.sub(Note_Rule, "", code)
			#print(code)

			#read each words and save them
			words = []
			words = create_tokens(code)
			vocabs = list(set(words))
			#print(vocabs)

			#write vocabs into vocabulary
			f = open("index.txt","r")
			vocabulary = f.read().split("\n")
			#print(vocabulary)
			f.close()
			for vocab in vocabs:
				if vocab == "\n" or vocab == " ":
					continue
				if vocab not in vocabulary:
					vocabulary.append(vocab)
			f = open("index.txt","w")
			f.write("\n".join(vocabulary))
			f.close()

			#transfer code file into data
			data = []
			for word in words:
				if word == "\n":
					data.append("0")
				else:
					data.append(str(vocabulary.index(word)))
			#print(data)
			f = open(".\\Data"+"\\"+str(codefile)+".txt","w")
			f.write("\n".join(data))
			f.close()

	print("success!")


#make_vocabulary()
