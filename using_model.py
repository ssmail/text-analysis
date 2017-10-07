# coding=utf-8
import sys
from gensim.models import KeyedVectors

reload(sys)
sys.setdefaultencoding('utf-8')

model = KeyedVectors.load_word2vec_format(
    r'/Users/weidian2015082404/PycharmProjects/gensim/model/santi_word2vec_binary.bin', binary=True, encoding='utf-8')

x = model.most_similar(positive=[u'程心'], topn=10)


for i in x:
    print i[0], i[1]
#
# print model.most_similar(negative=['智子', '三体'], topn=10)
#
# print model.most_similar(positive=['面壁计划'], negative=['智子', '三体'], topn=10)



# 计算两个词语的共现性
# print(model.similarity('智子', '面壁计划'))
# print(model.similarity('智子','三体'))

# 展开一个词的词向量
# print(model.word_vec('智子'))
# print(model['智子'])

# 查找不合群的词
# print(model.doesnt_match(['科学边界','基础物理','智子锁死','智子锁死','太空军']))

#
# print(help(model.evaluate_word_pairs))

# print(len(model.vocab))
