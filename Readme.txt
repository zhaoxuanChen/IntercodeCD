
1、获取切片文件-slice.txt
2、获取对应的标签文件-slice-label.txt
3、执行get_some_slices.py将slice.txt按每800个切片一个文件划分出若干个文件，如：slice_800-1.txt slice_800-2.txt
以 slice_800-1.txt为例执行后续步骤
4、执行1-dataprocess-代码补全.py  补全切片代码并将每个切片划分为compcode/function_i.txt
5、执行1.1-剔除不存在语义关系的代码.py  剔除不存在语义关系的语句final_compcode/function_i.txt
6、用joern解析final_compcode/下的代码
7、执行2-command-批量得到dot和node.py  得到每个切片的dot和node文件   dot_file/  node_file   link_file/
8、执行3-dataprocess-DFS遍历cfg.py     DFS_sequence/
9、执行4-generate_w2v_corpus.py  先映射，之后得到切片语料库和每个切片的token文件       corpus.pkl  Token_sequence/
10、执行5-word2vec.py 训练语料库并且将切片转为向量     wordmodel    input_cod.pkl
11、执行6-dealrawdata.py 截断与填充数据    train.pkl
12、将train_1.pkl输入模型