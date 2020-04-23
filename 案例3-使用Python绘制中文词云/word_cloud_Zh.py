#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()
text = open('xiyouji.txt','r',encoding='utf-8').read()

# Generate a word cloud image
wordcloud = WordCloud(font_path="simhei").generate(text)

# Display the generated image:
# the matplotlib way:

import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(font_path="simhei",max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()