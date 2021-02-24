#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3


# In[2]:


def t2s(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# In[ ]:




