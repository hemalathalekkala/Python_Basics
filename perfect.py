#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if n==s:
    print("Perfect Number")
else:
    print("Not Perfect Number")


# In[ ]:




