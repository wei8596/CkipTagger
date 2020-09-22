# -*- coding: UTF-8 -*-

# WS(斷詞), POS(詞性標注), NER(實體辨識)
from ckiptagger import WS, POS, NER
import pandas as pd

modelPath = 'C:/Users/wmmkslab/Desktop/CKIP/data'
ws = WS(modelPath)
pos = POS(modelPath)
ner = NER(modelPath)
newsPath = 'udnNews/news.xlsx'

if __name__ == '__main__':
    df = pd.read_excel(newsPath, usecols='B:F')
    while 1:
        numInput = input('select one content(1~1000): ')
        if numInput.isdigit():
            numInput = int(numInput)
            numInput -= 1
            break
        else:
            print('please input a number(1~1000)!')

    # remove '\n', '\r'
    content = ''
    for i in df['Content'][numInput]:
        if i != '\n' and i != '\r':
            content += i

    # WS
    word_s = ws([content],
                sentence_segmentation=True,
                segment_delimiter_set={'?', '？', '!', '！', '。', ',',
                                       '，', ';', ':', '、', '／'})
    #print('WS')
    #print(word_s)

    # POS
    word_p = pos(word_s)
    #print('POS')
    #print(word_p)

    # NER
    word_n = ner(word_s, word_p)
    #print('NER')
    #print(word_n)

    print(content)
    print(word_s)
    print(word_p)
    print(word_n)
