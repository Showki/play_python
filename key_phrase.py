import urllib.request
import urllib.parse
import json
from pprint import pprint

url = "http://jlp.yahooapis.jp/KeyphraseService/V1/extract"
params = {
        'appid':'dj0zaiZpPTRFTXJRWm80VDROWCZzPWNvbnN1bWVyc2VjcmV0Jng9MzI-',
        'sentence':'本堂と境内にいる「夫婦カツラ」が盛岡市の文化財として指定されている寺はどこですか。',
        'output':'json'
        }
url += "?" + urllib.parse.urlencode(params)
res = urllib.request.urlopen(url)

result = json.loads(res.read().decode('utf-8'))
pprint(result)



