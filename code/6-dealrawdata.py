## coding: utf-8
'''
该python文件用于数据训练CNN模型
This python file is used to train data in CNN model
================================================================
原始文件：BLSTM/keras_precision_recall/blstm_train_test.py
代码原著：Sophie
代码修改：Yoki
语言：Python 2.7
编写时间：2018.05.09

Original file: BLSTM/keras_precision_recall/blstm_train_test.py
Original coder: Sophie
coder: Yoki
Language: Python 2.7
Date: 2018.05.09
================================================================
Log
-------------------------------------
* 2018.01.21  Yoki
original version to train CNN
* 2018.05.09  Yoki
modify for do shuffle to data
'''

from __future__ import absolute_import
from __future__ import print_function
import pickle
#import cPickle
import numpy as np
import random
import time
import math
import os
from collections import Counter
#from imblearn.ensemble import BalanceCascade
#from imblearn.over_sampling import ADASYN
#from imblearn.over_sampling import SMOTE


np.random.seed(1337)  # for reproducibility

'''
dealrawdata function
-----------------------------
线下对数据集进行截断和打乱处理并保存为pkl文件
This function is used to cut the dataset, do shuffle and save into pkl file.

# Arguments
    raw_traindataSet_path: String type, the raw data path of train set
    raw_testdataSet_path: String type, the raw data path of test set
    traindataSet_path: String type, the data path to save train set
    testdataSet_path: String type, the data path to save test set
    batch_size: Int type, the mini-batch size
    maxlen: Int type, the max length of data
    vector_dim: Int type, the number of data vector's dim

'''
def dealrawdata(raw_traindataSet_path,traindataSet_path,batch_size, maxlen, vector_dim):
    print("Loading data...")
    start = time.time()
    for filename in os.listdir(raw_traindataSet_path):
        X_train, train_labels= load_data_binary(raw_traindataSet_path + filename, batch_size, maxlen=maxlen, vector_dim=vector_dim)
        np.random.seed(113)
        np.random.shuffle(X_train)
        np.random.seed(113)
        np.random.shuffle(train_labels)
        f_train = open(traindataSet_path + filename, 'wb')
        pickle.dump([X_train, train_labels], f_train)
        f_train.close()
        end = time.time()
        print(end - start)
 

def load_data_binary(dataSetpath, batch_size, maxlen=None, vector_dim=40, seed=113):   
    #加载数据 
    f1 = open(dataSetpath, 'rb')
    X, ids = pickle.load(f1)
    f1.close()

    cut_count = 0
    fill_0_count = 0
    no_change_count = 0
    fill_0 = [0]*vector_dim
    if maxlen:
        new_X = []
        for x, i in zip(X, ids):
            if len(x) <  maxlen:
                x = x + [fill_0] * (maxlen - len(x))
                new_X.append(x)
                fill_0_count += 1

            elif len(x) == maxlen:
                new_X.append(x)
                no_change_count += 1
                    
            else:
                startpoint = 0
                endpoint =  maxlen
                new_X.append(x[startpoint:endpoint])
                #cut_count += 1
        X = new_X

    return X, ids



if __name__ == "__main__":
    batchSize = 16
    vectorDim = 40
    maxLen = 500
    raw_traindataSetPath = "raw_train/"
    #raw_testdataSetPath = "./dl_input/cdg_ddg1/test_all/"
    traindataSetPath = "deal_train/"
    #testdataSetPath = "./dl_input/cdg_ddg1/all_new/"
    dealrawdata(raw_traindataSetPath,  traindataSetPath,  batchSize, maxLen, vectorDim)
    #dealrawdata(raw_traindataSetPath,traindataSetPath, batchSize, maxLen, vectorDim)
