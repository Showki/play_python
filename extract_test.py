
import MeCab
import collections
import json
import urllib


mecab = MeCab.Tagger('mecabrc')

def tokenize(text):
    #mecab.parse('')#文字列がGCされるのを防ぐ
    node = mecab.parseToNode(text)
    words = {}
    #words = collections.OrderedDict()
    i = 0
    while node:
        #単語を取得
        word = node.surface
        #品詞を取得
        #品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
        pos = node.feature.split(",")[0]
        words[i] = {word : pos}
        #次の単語に進める
        node = node.next
        i += 1
    return words

#text = input()



if __name__ == '__main__':
    sentence = "本堂と境内にいる「夫婦カツラ」が盛岡市の文化財として指定されている寺はどこですか。"
    answer = "援交寺"
    analyzed_sentence = tokenize(sentence)
    analyzed_answer = tokenize(answer)
    print(analyzed_answer,analyzed_sentence)


