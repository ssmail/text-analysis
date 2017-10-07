# coding=utf-8

from gensim.models import Word2Vec
import jieba
import re
import multiprocessing
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def diydict():
    path = '/Users/weidian2015082404/PycharmProjects/gensim/diy.txt'
    dictionary = open(path, 'r')
    dict = []
    for word in dictionary:
        word = word.strip('\n')
        dict.append(word)

    print dict
    return dict


class MySentence(object):
    def __init__(self, filename):
        self.filename = filename
        for word in diydict():
            jieba.add_word(word, 10)

    def __iter__(self):
        lines = open(self.filename, 'r').readlines()
        for line in lines:
            if (len(line)):
                wordlist = list(jieba.cut(line))
                yield wordlist


start = time.time()
MySentences = MySentence(filename=r'/Users/weidian2015082404/PycharmProjects/gensim/s.txt')
model = Word2Vec(sentences=MySentences,
                 size=200,
                 window=10,
                 min_count=10,
                 workers=multiprocessing.cpu_count())

model.wv.save_word2vec_format(fname=r'/Users/weidian2015082404/PycharmProjects/gensim/model/santi_word2vec_binary.bin',
                              binary=True)
end = time.time()
print(end - start)
