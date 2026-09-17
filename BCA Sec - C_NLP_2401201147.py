#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install nltk')


# In[8]:


from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')


# In[9]:


text = "Ram is a good cook, but he can not make pulses"
payal = word_tokenize(text)
print(payal)


# In[10]:


text = """ram is a good cook.
He is only 18 years old. his ph no. is 87587668"""

payal = sent_tokenize(text)
payal


# In[12]:


import string
text = "he is ^%#$ and full of life ?>(*&"
payal = word_tokenize(text)
print(payal)
words = []
for i in payal:
    if i not in string.punctuation:
        words.append(i)
print(words)        


# In[14]:


from nltk.corpus import stopwords
nltk.download('stopwords')

text = "Ram is a good cook, but ha can not make pulses."
payal = word_tokenize(text)
words = []
for i in payal:
    if i.lower() not in stopwords.words('english'):
        words.append(i)
print(words)


# In[15]:


get_ipython().system('pip install pyspellchecker')
from spellchecker import SpellChecker
spell = SpellChecker()
text = "i havv a gud, bd, and ugly situton"
payal = text.split()
correct = []
for i in payal:
    correct.append(spell.correction(i))
    
print(correct)    


# In[16]:


get_ipython().system('pip install textblob')
from textblob import TextBlob
text = "i havv a gud, bd, and ugly situton."
correct = str(TextBlob(text).correct())
print(correct)


# In[ ]:




