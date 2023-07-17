# 打开并读取.npy文件
import numpy as np
# 导入npy文件所在路径
adj = np.load('GPCR/dataset/GPCR_train/word2vec_30/adjacencies.npy',allow_pickle=True)
compounds = np.load('GPCR/dataset/GPCR_train/word2vec_30/compounds.npy',allow_pickle=True)
interactions = np.load('GPCR/dataset/GPCR_train/word2vec_30/interactions.npy',allow_pickle=True)
proteins = np.load('GPCR/dataset/GPCR_train/word2vec_30/proteins.npy',allow_pickle=True)

# print(adj)
print(compounds)
# print(interactions)
# print(proteins)


