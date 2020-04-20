#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np


# In[42]:


payment10=np.zeros((100000,1))

for i in range(100000):
    coins = np.random.choice(np.arange(start = 1, stop = 11), 10, replace = False)
    payment10[i]= coins[0]
    for j in range(9):
        payment10[i] = payment10[i] + np.absolute(coins[j+1]-coins[j])


# In[43]:


avg = payment10.mean()
std = payment10.std()


# In[44]:


print("Average payment for% 2d coins is% 5.5f and standard deviation is% 5.5f" %(len(coins),avg, std))  


# In[48]:


payment20=np.zeros((1000000,1))

for i in range(1000000):
    coins = np.random.choice(np.arange(start = 1, stop = 21), 20, replace = False)
    payment20[i]= coins[0]
    for j in range(19):
        payment20[i] = payment20[i] + np.absolute(coins[j+1]-coins[j])


# In[49]:


avg = payment20.mean()
std = payment20.std()


# In[51]:


print("Average payment for% 2d coins is% 5.5f and standard deviation is% 5.5f" %(len(coins),avg, std))  


# In[52]:


prob10 = sum(payment10>=45)/len(payment10)
prob20 = sum(payment20>=160)/len(payment20)


# In[53]:


print("Probablity of payment >= 45 for 10 coins is% 5.5f and probablity of payment >= 160 for 20 coins is% 5.5f" %(prob10, prob20))  





