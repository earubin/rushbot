#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import datetime 
from twilio.rest import Client
import logging
logging.basicConfig(filename = 'txt.log', level = logging.WARNING, format = '%(asctime)s:%(levelname)s:%(message)s')


# In[2]:


get_ipython().run_line_magic('store', '-r account_sid')
get_ipython().run_line_magic('store', '-r auth_token')


# In[3]:


client = Client(account_sid, auth_token)


# In[4]:


class TextBot():
    
    def __init__(self, _sid, _token, from_number, to_number, *args, **kwargs):
            self._sid = _sid
            self._token = _token
            self.message = kwargs.get('message')
            self.from_number = from_number
            self.to_number = to_number
            self.args = args
            self.kwargs = kwargs
            self._sid_tracker = []
            
    def send_message(self, message):
        self.message = message
        resp = input('Do you want to send this message?' + '\n')
        if resp.lower() == 'yes' and (self.to_number and len(self.to_number.replace(' ', '')) == 12):
                self.message = client.messages                     .create(
                        body = message,
                        from_ = self.from_number,
                        to = self.to_number)
                if len(self.args) > 0:
                    for i in self.args:
                        self.message = client.messages.create(
                            body = message,
                            from_ = self.from_number,
                            to = i)
                self._sid_tracker.append(self.message.sid)
        else:
            print('Authentication failed.')
            
    def set_to(self, to_number):
        self.to_number = to_number
    
    def set_from(self, from_number):
        self.from_number = from_number
        
    def get_to(self):
        return self.to_number
    
    def get_from(self):
        return self.from_number


