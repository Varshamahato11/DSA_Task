#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right


# In[2]:





# In[ ]:





# In[ ]:




