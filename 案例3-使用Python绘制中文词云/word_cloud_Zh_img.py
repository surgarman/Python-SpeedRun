#!/usr/bin/python3.5
#-*- coding: utf-8 -*-
"""
Using custom colors
====================
Using the recolor method and custom coloring functions.
"""

import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
import os

from wordcloud import WordCloud, STOPWORDS


plt.rcParams['font.sans-serif']=['SimHei']
#⽤来正常显示中⽂标签
plt.rcParams['axes.unicode_minus']=False
#⽤来正常显示负号 #有中⽂出现的情况，需要u'内容'

font=os.path.join(os.path.dirname(__file__), "simhei")

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname(__file__)


mask = np.array(Image.open(path.join(d, "timg.png")))


text = open('xiyouji.txt','r',encoding='utf-8').read()

# preprocessing the text a little bit
text = text.replace("行者道", "行者")
text = text.replace("八戒道", "八戒")
text = text.replace("沙僧道", "沙僧")
text = text.replace("三藏道", "三藏")

# adding movie script specific stopwords
stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

wc = WordCloud(font_path=font,max_words=2000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(text)
# store default colored image
default_colors = wc.to_array()
plt.title("西游记-词频统计")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3))


wc.to_file("a_new_hope.png")
plt.axis("off")
plt.figure()
plt.title("西游记-词频统计")
plt.imshow(default_colors)
plt.axis("off")
plt.show()