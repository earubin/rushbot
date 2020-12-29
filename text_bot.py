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
                        self.message = client.messages                         .create(
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


# In[5]:


'''

Put whatever names you want to text in here. I will organize this a little better at some point, but for now, it's just two arrays zipped into a dictionary.


names = ['Jack Aiello', 'Ben Goddard', 'Daniel Glassman', 'Brian Carter', 
         'Jimmy Ewers', 'Ryan Way', 'Daniel Gankov', 'Jack Gillespie', 
         'Ronan Kenkare', 'Wyatt Flynn', 'Jack Banks', 'Elliot Rubin']

numbers = ['+12244564568', '+16193940968', '+18477511005', '+16302546002',
           '+17083051183', '+18155923507', '+17736033201', '+18474527048',
           '+15857058332', '+17082651576', '+17735755623', '+18479242986']

nums_dict = dict(zip(names, numbers))
#bot = TextBot(account_sid, auth_token, '+12705944959', '+18479242986', [i for i in nums_dict.values() if i != nums_dict['Elliot Rubin']])

'''


# In[7]:


bot = TextBot(account_sid, auth_token, '+12705944959', '+12244564568')
bot.send_message('Good morning, king. Make sure you complete your task for today.' + '\n' + '\n' +
                 'This message is automated and I cannot yet see your replies.')


# In[17]:


a = datetime.datetime.today()
numdays = 10
date_list = []
for x in range (0, numdays):
    date_list.append(a + datetime.timedelta(days = x))
date_list


# In[11]:


new_bot = TextBot(account_sid, auth_token, '+12705944959', nums_dict['Jack Aiello'])
new_bot.send_message('Can you massage my back?')


# In[ ]:


#while datetime.datetime.today() < date_list[len(date_list) - 1]:
    #if datetime.datetime.today().time() == datetime.time(9,0,0) or datetime.datetime.today().time() == datetime.time(15,0,0) or datetime.datetime.today().time() == datetime.time(18,0,0):
        #new_bot.send_message('Good morning, king. Make sure you complete your task for today.' , '\n', '\n' ,
                             #'This message is automated and I cannot yet see your replies.')

