#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system(' pip install googletrans==3.1.0a0')


# In[1]:


import speech_recognition
import tempfile
from gtts import gTTS
from pygame import mixer
from googletrans import Translator


# In[2]:


def listenTo():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    return r.recognize_google(audio, language = 'zh-TW')


# In[3]:


def speak(sentence, lang):
    mixer.init()
    with tempfile.NamedTemporaryFile(delete = True) as fp:
        tts = gTTS(text = sentence, lang = lang)
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()


# In[4]:


translator = Translator()
translator.translate('大家好', dest = 'en').text


# In[5]:


lang = 'ja'
A = translator.translate(listenTo(), lang).text
speak(A, lang)
print(A)
B = translator.translate(A, dest = 'ja')
print(B)


# In[7]:


lang = 'ko'
A = translator.translate(listenTo(), lang).text
speak(A, lang)
print(A)
B = translator.translate(A, dest = 'ko')
print(B)


# In[8]:


import googletrans
from pprint import pprint
pprint(googletrans.LANGCODES)


# In[9]:


unknown_sentence = 'สวัสดีตอนเช้า'
results = translator.detect(unknown_sentence)
print(results)
print(results.lang)


# In[ ]:




