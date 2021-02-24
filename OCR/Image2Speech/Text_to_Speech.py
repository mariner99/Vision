#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from gtts import gTTS
from playsound import playsound


# In[9]:


text = input()
tts = gTTS(text)
tts.save("input.mp3")


# In[10]:


playsound('/Users/SarthakPratik/input.mp3')


# In[ ]:




