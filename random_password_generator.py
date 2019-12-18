#!/usr/bin/env python
# coding: utf-8

# In[1]:


# random password generator
import random
characters_sa='abcdefghijklmnopqrstuvwxyz'
characters_la='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
integers='0123456789'
special_sym='!@#$%^&*_+-,./\?~`='

characters=characters_sa+characters_la+integers+special_sym

c=1
i=1
print("enter length of password")
len=int(input())

print("enter number of passwords")
no=int(input())

for i in range(no):
    password=''
    for c in range(len):
        password+=random.choice(characters)
    print(password)


# In[ ]:




