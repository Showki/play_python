import MeCab
mecab = MeCab.Tagger('mecabrc')
#UnicodeDecodeError回避a)
mecab.parse('')

def tokenize(text):
    #mecab.parse('')#文字列がGCされるのを防ぐ
    node = mecab.parseToNode(text)
    words = []
    node = node.next
    while node:
        #単語を取得
        word = node.surface
        #品詞を取得
        #品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
        pos = node.feature.split(",")[0]
        words.append([word,pos])
        node = node.next
    words.pop()
    return words

def concatenateNoun(tokenized_text):
    composite_noun = ''
    for word in tokenized_text:
        if word[1] == '名詞':
            composite_noun += word[0]
        else:


    return type(tokenized_text)

if __name__ == '__main__':
    sentence = "本堂と境内にいる「夫婦カツラ」が盛岡市の文化財として指定されている寺はどこですか。"
    answer = "援交寺"
    result_sentence = concatenateNoun(tokenize(sentence))
    #result_sentence = tokenize(sentence)
    result_answer = concatenateNoun(tokenize(answer))
    #result_answer = tokenize(answer)
    print(result_sentence[1],result_answer[1])


