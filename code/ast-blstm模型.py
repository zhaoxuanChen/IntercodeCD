## coding: utf-8
'''
该python文件用于最终大数据集训练BGRU模型,注意文件写入可能需要sudo权限
This python file is used to train four class focus data in blstm model
================================================================
原始文件：BLSTM/keras_precision_recall/blstm_train_test.py
代码原著：Sophie
代码修改：Yoki
语言：Python 2.7
编写时间：2018.01.25

Original file: BLSTM/keras_precision_recall/blstm_train_test.py
Original coder: Sophie
coder: Yoki
Language: Python 2.7
Date: 2018.01.25
================================================================
Log
-------------------------------------
* 2018.01.25  Yoki
original version to train LSTM
'''

from keras.preprocessing import sequence
from keras.optimizers import SGD, RMSprop, Adagrad, Adam, Adadelta
from keras.models import Sequential, load_model
from keras.layers.core import Masking, Dense, Dropout, Activation
from keras.layers.recurrent import LSTM,GRU
from preprocess_dl_Input import *
from keras.layers.wrappers import Bidirectional
from collections import Counter
import numpy as np
import pickle
import random
import time
import math
import os


RANDOMSEED = 2018  # for reproducibility
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = ""


def build_model(maxlen, vector_dim, layers, dropout):
    print('Build model...')
    model = Sequential()
    
    model.add(Masking(mask_value=0.0, input_shape=(maxlen, vector_dim)))
    
    for i in range(1, layers):
        model.add(Bidirectional(LSTM(units=128, activation='tanh', recurrent_activation='hard_sigmoid', return_sequences=True)))
        model.add(Dropout(dropout))
        
    model.add(Bidirectional(LSTM(units=128, activation='tanh', recurrent_activation='hard_sigmoid')))
    model.add(Dropout(dropout))
    
    model.add(Dense(1, activation='sigmoid'))
          
    model.compile(loss='binary_crossentropy', optimizer='adamax', metrics=['TP_count', 'FP_count', 'FN_count', 'precision', 'recall', 'fbeta_score'])
    
    model.summary()
 
    return model


def main(traindataSet_path, testdataSet_path, realtestpath, weightpath, resultpath, batch_size, maxlen, vector_dim, layers, dropout):
    print("Loading data...")
    
    model = build_model(maxlen, vector_dim, layers, dropout)
    
    #如果需要加载模型
    #model.load_weights(weightpath)
    
    print("Train...")
    dataset = []
    labels = []
    for filename in os.listdir(traindataSet_path):
        #if "api" not in filename and "array" not in filename and "expr" not in filename and "pointer" not in filename:
        #    continue
        print(filename)
        f = open(os.path.join(traindataSet_path, filename),"rb")
        dataset_file,labels_file= pickle.load(f)
        f.close()
        dataset += dataset_file[0:8000]
        labels += labels_file[0:8000]
    print(len(dataset), len(labels))
    
    #训练集的labels没有转成二元，需要先转成0和1
    #bin_labels = []
    #for label in labels:
    #    bin_labels.append(multi_labels_to_two(label))
    #labels = bin_labels
        
    #由于是四类混合数据，需要打乱
    np.random.seed(RANDOMSEED)
    np.random.shuffle(dataset)
    np.random.seed(RANDOMSEED)
    np.random.shuffle(labels)

    #生成训练生成器
    train_generator = generator_of_data(dataset, labels, batch_size, maxlen, vector_dim)    
    all_train_samples = len(dataset)
    steps_epoch = int(all_train_samples / batch_size)

    #开始训练
    t1 = time.time()
    model.fit_generator(train_generator, steps_per_epoch=steps_epoch, epochs=4)
    t2 = time.time()
    print(t2-t1)

    
    model.save_weights(weightpath)
    
    #如果需要加载模型
    model.load_weights(weightpath)
    print(testdataSet_path)
    print("Test...")
    dataset = []
    labels = []
    funcs = []
    testcases = []
    for filename in os.listdir(testdataSet_path):
        #if "api" not in filename and "array" not in filename and "expr" not in filename and "pointer" not in filename:
        #    continue
        #print(filename)
        f = open(os.path.join(testdataSet_path, filename),"rb")
        datasetfile,labelsfile= pickle.load(f)
        f.close()
        dataset += datasetfile[8000:10000]
        labels += labelsfile[8000:10000]
    print(len(dataset), len(labels))
    '''
    #测试集的labels没有转成二元，需要先转成0和1
    bin_labels = []
    for label in labels:
        bin_labels.append(multi_labels_to_two(label))
    labels = bin_labels
    '''    
    #测试模型
    batch_size = 16
    test_generator = generator_of_data(dataset, labels, batch_size, maxlen, vector_dim)
    all_test_samples = len(dataset)
        
    TP, FP, TN, FN, TP_indexs, FP_indexs, FN_indexs = 0, 0, 0, 0, [], [],[]
    #对于每一mini-batch样本做测试
    for i in range(math.floor(len(dataset)/batch_size)):
        print("\r", i, "/", math.floor(len(dataset)/batch_size), end="")
        #测试输入
        test_input = next(test_generator)
        #深度学习模型的序列输出
        layer_output = model.predict_on_batch([test_input[0]])
        #测试结果
        for index in range(batch_size):
            y_pred = 1 if layer_output[index] >= 0.5 else 0

            if y_pred == 0 and labels[i*batch_size+index] == 0:
                TN += 1
            if y_pred == 0 and labels[i*batch_size+index] == 1:
                FN += 1
                FN_indexs.append(i*batch_size+index)
            if y_pred == 1 and labels[i*batch_size+index] == 0:
                FP += 1
                FP_indexs.append(i*batch_size+index)
            if y_pred == 1 and labels[i*batch_size+index] == 1:
                TP += 1
                TP_indexs.append(i*batch_size+index)
    
    f = open("TP-0.4-ddg_index_sysevr.pkl",'wb')
    pickle.dump(TP_indexs, f)
    f = open("FP-0.4-ddg_index_sysevr.pkl",'wb')
    pickle.dump(FP_indexs, f)
    f = open("FN-0.4-ddg_index_sysevr.pkl",'wb')
    pickle.dump(FN_indexs, f)
    f.close()
    
    #TN = all_test_samples - TP - FP - FN
    fwrite = open(resultpath, 'a')
    fwrite.write('SARD: ' + str(30000) + ' ' + str(all_test_samples) + '\n')
    fwrite.write("TP:" + str(TP) + ' FP:' + str(FP) + ' FN:' + str(FN) + '\n')
    FPR = float(FP) / (FP + TN)
    fwrite.write('FPR: ' + str(FPR) + '\n')
    FNR = float(FN) / (TP + FN)
    fwrite.write('FNR: ' + str(FNR) + '\n')
    Accuracy = float(TP + TN) / (all_test_samples)
    fwrite.write('Accuracy: ' + str(Accuracy) + '\n')
    precision = float(TP) / (TP + FP)
    fwrite.write('precision: ' + str(precision) + '\n')
    recall = float(TP) / (TP + FN)
    fwrite.write('recall: ' + str(recall) + '\n')
    f_score = (2 * precision * recall) / (precision + recall)
    fwrite.write('fbeta_score: ' + str(f_score) + '\n')
    fwrite.write('--------------------\n')
    fwrite.close()    #return
    '''
    #记录报为有漏洞的函数
    dict_testcase2func = {}
    for i in testcases:
        if not i in dict_testcase2func:
            dict_testcase2func[i] = {}
    
    for i in TP_indexs:
        if funcs[i] == []:
            continue
        for func in funcs[i]:
            if func in dict_testcase2func[testcases[i]].keys():
                dict_testcase2func[testcases[i]][func].append("TP")
            else:
                dict_testcase2func[testcases[i]][func] = ["TP"]
    
    for i in FP_indexs:
        if funcs[i] == []:
            continue
        for func in funcs[i]:
            if func in dict_testcase2func[testcases[i]].keys():
                dict_testcase2func[testcases[i]][func].append("FP")
            else:
                dict_testcase2func[testcases[i]][func] = ["FP"]
    f = open(resultpath+"_dict_testcase2func.pkl",'wb')
    print('open')
    #pickle.dump(dict_testcase2func, f)
    pickle.dump(dict_testcase2func, f)
    f.close()
    
        #保存漏报样本的标签值以及漏报样本和误报样本的四类分类
        FP_index = result[1]    #误报
        FN_index = result[2]    #漏报
        #漏报样本索引值转换为标签值
        f = open(filename,"rb")
        dataset,labels = cPickle.load(f)
        f.close()
        FN_label = []
        for i in FN_index:
            FN_label.append(labels[i])
        f = open(resultpath+"_FN_label.pkl","wb")
        cPickle.dump(FN_label,f,protocol=cPickle.HIGHEST_PROTOCOL)
        f.close()
        
        #漏报样本的四类分类
        FN_class = []
        for i in FN_index:
            if i in range(0,3952):
                FN_class.append("expr")
            if i in range(3952,3952+6496):
                FN_class.append("array")
            if i in range(3952+6496,3952+6496+6096):
                FN_class.append("api")
            if i in range(3952+6496+6096,3952+6496+6096+19760):
                FN_class.append("pointer")
        f = open(resultpath+"_FN_class.pkl","wb")
        cPickle.dump(FN_class,f,protocol=cPickle.HIGHEST_PROTOCOL)
        f.close()
        #误报样本的四类分类
        FP_class = []
        for i in FP_index:
            if i in range(0,3952):
                FP_class.append("expr")
            if i in range(3952,3952+6496):
                FP_class.append("array")
            if i in range(3952+6496,3952+6496+6096):
                FP_class.append("api")
            if i in range(3952+6496+6096,3952+6496+6096+19760):
                FP_class.append("pointer")
        f = open(resultpath+"_FP_class.pkl","wb")
        cPickle.dump(FP_class,f,protocol=cPickle.HIGHEST_PROTOCOL)
        f.close()
    '''
def testrealdata(realtestpath, weightpath, batch_size, maxlen, vector_dim, layers, dropout):
    #加载模型
    model = build_model(maxlen, vector_dim, layers, dropout)
    model.load_weights(weightpath)
    
    #加载数据
    print("Loading data...")
    for filename in os.listdir(realtestpath):
        print(filename)
        f = open(realtestpath+filename, "rb")
        realdata = pickle.load(f,encoding="latin1")
        f.close()
    
        labels = model.predict(x = realdata[0],batch_size = 1)
        for i in range(len(labels)):
            if labels[i][0] >= 0.5:
                print(realdata[1][i])


if __name__ == "__main__":
    batchSize = 16
    vectorDim = 40
    maxLen = 500
    layers = 1
    dropout = 0.4
    traindataSetPath = "ast-train/"
    testdataSetPath = "ast-test/"
    realtestdataSetPath = "data/"
    weightPath = 'ast-model/finalepoch4'
    resultPath = "ast-result/finalepoch4"
    #dealrawdata(raw_traindataSetPath, raw_testdataSetPath, traindataSetPath, testdataSetPath, batchSize, maxLen, vectorDim)
    main(traindataSetPath, testdataSetPath, realtestdataSetPath, weightPath, resultPath, batchSize, maxLen, vectorDim, layers, dropout)
    #testrealdata(realtestdataSetPath, weightPath, batchSize, maxLen, vectorDim, layers, dropout)
