## coding: utf-8
from gensim.models.word2vec import Word2Vec
import pickle


def generate_w2vModel(decTokenFlawPath, w2vModelPath):
    #训练生成词向量
    #decTokenFlawPath是语料保存的路径，w2vModelPath是训练好的词向量
    f1 = open(decTokenFlawPath, 'rb')
    sentences = pickle.load(f1)
    f1.close()
    #print(sentences[0], sentences[1])
    model = Word2Vec(sentences=sentences, size=50, window=15, min_count=0, max_vocab_size=None, sample=0.001, seed=1, workers=1, min_alpha=0.001, sg=1, hs=0, iter=5)
    model.save(w2vModelPath)

    
def get_code(trainDataIDPath, w2vpath):
    model = Word2Vec.load(w2vpath)
    dl_corpus = []
    list_database=[]
    for i in range(1,10001):
        print(i)
        f = open(trainDataIDPath+"function_"+str(i)+".txt" )
        tokenlist=f.read().split(" ")[0:-1]
        #list_database.append(list_AST)
        print(tokenlist)
        dl_corpus.append([model[idx] for idx in tokenlist] )
    f = open("input_datae.pkl", 'wb')
    d = open("api_slices_label.pkl", 'rb')
    labels=pickle.load(d)
    print(len(labels))
    pickle.dump((dl_corpus, labels), f, True)
    f.close()
	
def main():
    #dec_tokenFlaw_path = 'corpus.pkl'
    #w2v_model_path = "w2vmodel/wordmodel"    
    #generate_w2vModel(dec_tokenFlaw_path, w2v_model_path)
    token_Path='Token_sequence/'
    w2vpath_2="w2vmodel/wordmodel"
    get_code(token_Path,w2vpath_2)
 
   
if __name__ == "__main__":
    main()


