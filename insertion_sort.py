#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Insertion Sort

'''
Sort a sequence of data in non-decreasing way
which always put the greater number in a 
subarray in its right place.
'''

def non_decreasing_insertion_sort(li):
    
    length = len(li)
    for i in range(1, length):
        key = li[i]
        j = i-1
        while j >= 0 and key < li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j + 1] = key
    return li

keys = list(map(int, input().split()))
print(non_decreasing_insertion_sort(keys))


# In[3]:


'''
Sort a sequence of data in non-increasing way
which always put the smaller number in a 
subarray in its right place.
'''

def non_increasing_insertion_sort(li):
    length = len(li)
    for i in range(length-2, -1, -1):
        j = i + 1
        key = li[i]
        while j < length and key < li[j]:
            li[j-1] = li[j]
            j += 1
        li[j-1] = key
    return li

keys = list(map(int, input().split()))
print(non_increasing_insertion_sort(keys))


# In[ ]:




