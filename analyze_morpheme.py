class AnalyzeMorpheme:
    def __init__(self,text):
        self.text = text

    def getTokenizedWords(self):
        import MeCab
        mecab = MeCab.Tagger('mecabrc')
        #UnicodeDecodeError回避a
        #mecab.parse('')#文字列がGCされるのを防ぐ
        mecab.parse('')
        node = mecab.parseToNode(self.text)
        words = []
        node = node.next
        while node:
            word = node.surface
            next_word = None
            #品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
            pos = node.feature.split(",")[0] #品詞だけ切取り
            if pos == '名詞':
                while node:
                    next_pos = node.next.feature.split(",")[0]
                    if next_pos == '名詞':
                        next_word = node.next.surface
                        word = word + next_word
                        node = node.next
                    else:
                        if next_word is not None:
                            pos = '複合名詞'
                        words.append([word,pos])
                        node = node.next
                        break
            else:
                words.append([word,pos])
                node = node.next
        words.pop()
        return words

if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    sentence = "本堂と境内にいる「夫婦カツラ」が盛岡市の文化財として指定されている寺はどこですか。"
    answer = "援交寺"
    
    morpheme = AnalyzeMorpheme(sentence)
    result_sentence = morpheme.getTokenizedWords() #()を外すと<bound method〜
    
    morpheme = AnalyzeMorpheme(answer)
    result_answer = morpheme.getTokenizedWords() #()を外すと<bound method〜
    
    result_answer = morpheme.getTokenizedWords()
    print(result_sentence,result_answer)
