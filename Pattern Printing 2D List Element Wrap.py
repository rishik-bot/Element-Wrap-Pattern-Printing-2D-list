#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Python3 Program to print rectangular inner reducing pattern 
  
# function to Print pattern  
def prints(a, size):  
    for i in range(size):  
        for j in range(size): 
            print(a[i][j], end = '') 
        print() 
  
# function to compute pattern  
def innerPattern(n):  
    # Pattern Size  
    size = 2 * n - 1
    front = 0
    back = size - 1
    a = [[0 for i in range(size)] for i in range(size)]
    
    while (n != 0):  
        for i in range(front, back + 1): 
            for j in range(front, back + 1): 
                if (i == front or i == back or
                    j == front or j == back): 
                    a[i][j] = n 
        front += 1
        back -= 1
        n -= 1
    prints(a, size);  
  
# Input  
n = int(input())
  
# function calling  
innerPattern(n) 


# In[6]:


n=int(input())
l0=[['1']]
size=n*2-1
for i in range(2,n+1):
    l1=[str(i)]*(2*i-3)
    l2=[str(i)]*(2*i-3)
    l0.insert(0,l1)
    l0.append(l2)
    for j in l0:
        j.insert(0,str(i))
        j.append(str(i))
l3=[]
for i in l0:
    l3.append("".join(i))
for i in l3:
    print(i)


# In[ ]:




