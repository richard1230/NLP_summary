# !/usr/bin/python3n
# code-python(3.6)
from sklearn.feature_extraction.text import TfidfVectorizer

# 功能：原始文本转化为tf - idf的特征矩阵，从而为后续的文本相似度计算，奠定基础

document = ['This is a dog!', 'that is an ...apple.']
'''
这里有两个文档，文档0是‘this is a dog’，文档1是’that is a cat’。每个文档都是一个样本点。
'''

model = TfidfVectorizer().fit(document)
'''
(1)   fit()会先分析语料库，提取词典等；
(2)   从两个文档中，将所有大写转小写，去掉所有符号，再分别提出的词语集合['this', 'is', 'a', 'dog']，['that', 'is', 'an', 'apple']。
(3)   对两个集合去重，得到[‘a','an', 'apple', 'dog', 'is', 'that', 'this']。但这里面有的词语不在该语料库中，比如'a'，要剔除，得到词语集合['an', 'apple', 'dog', 'is', 'that', 'this']，每个词语都是一个特征。
'''

print(model.get_feature_names())
'''
从文档中提取的词语(特征) = ['an', 'apple', 'dog', 'is', 'that', 'this']
'''

print(model.vocabulary_)
'''
返回词语与索引 = {'an': 0, 'apple': 1'，dog': 2,'is': 3,'that': 4, 'this': 5}，表示'an'是第一个特征，'apple'是第二个特征，'this'是最后一个特征，共6个特征。
'''

print(model.idf_)
'''
[1.40 1.40 1.40 1  1.40 1.40]
'''
matrix = model.transform(document)  # transform()会把每篇文档转换为向量；得到tf-idf矩阵；

print(matrix.shape)  # 矩阵是2行6列；即有2个文档，每个文档有6个词语(特征)

print(matrix)
'''
稀疏矩阵表示法
(0, 5)	0.63	#文档0的第5个特征this的权重值是0.63
(0, 3)	0.44
(0, 2)	0.63
(1, 4)	0.53	#文档1的第4个特征that的权重值是0.53
(1, 3)	0.37
(1, 1)	0.53
(1, 0)	0.53
'''
print(matrix.todense())  # 转化为更直观的一般矩阵
'''
[[0      0      0.63    0.44   0.     0.63]
 [0.53   0.53   0       0.37   0.53   0   ]]
'''