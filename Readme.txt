1, get slice file slice. TXT

2. Get the corresponding label file -slice-label.txt

Get_some_slices. Py divides slice. TXT into several files, such as slice_800-1.txt slice_800-2.txt, according to one file per 800 slices

Take slice_800-1.txt as an example to perform the next steps

4. Perform 1-dataprocess-code completion. Py completes the section code and divides each section into compcode/function_i.txt

5. Perform 1.1- cull the code with no semantic relationship. Py culls the statement final_compcode/function_i.txt with no semantic relationship

6. Use joern to parse the code under final_compcode/

7. Execute 2-command-batch to get dot and node.py to get dot_file/ node_file link_file/ for each slice

8. Perform 3-dataprocess-dfs traversal of cfg.py DFS_sequence/

9. Map 4-generate_w2v_corpus. Py first, and then get the corpus of slices and the token file corpus. PKL Token_sequence/ of each slice

10. Perform the 5-word2vec.py training corpus and convert the slices into the vector wordmodel input_cod.pkl

11. Execute 6-dealrawdata.py to truncate and populate data train.pkl

12. Train_1.pkl was input into the model

