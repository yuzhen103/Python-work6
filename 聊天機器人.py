#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install winspeech')


# In[2]:


get_ipython().system(' pip install SpeechRecognition')


# In[3]:


get_ipython().system(' pip install pipwin')


# In[3]:


import speech_recognition
def listenTo():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    return r.recognize_google(audio, language = 'zh-TW')


# In[4]:


import tempfile
from gtts import gTTS
from pygame import mixer
mixer.init()


# In[5]:


def speak(sentence):
    with tempfile.NamedTemporaryFile(delete = True)as fp:
        tts = gTTS(text = sentence, lang = 'zh-TW')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()
speak('大家好')


# In[14]:


qa = {'早安':'早安甄甄，今天又是美好的一天','午安':'又賴床了，快點去贖罪','晚安':'晚安甄甄，祝好夢'}


# In[15]:


speak(qa.get(listenTo(),'沒聽懂，再說一次'))


# In[ ]:




