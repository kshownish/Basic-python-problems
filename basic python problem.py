#!/usr/bin/env python
# coding: utf-8

# Create a random vector of size 30 and find the mean value

# In[2]:


import numpy as np  
x = np.random.random(30)
print("Random vector=",x)
print("Mean value=",x.mean())


# Create a NumPy array having elements 0 to 10 And negate all the elements between 3 and 9

# In[7]:


import numpy as np
arr = np.arange(0,10)   
print("Numpy array=",arr)
index=[np.arange(3,10)]
x = np.delete(arr, index)
print("Final array after negating=",x)


#  Create a random array of 3 rows and 3 columns and sort it according to the first, second, or third 
# column

# In[9]:


import numpy as np
x =[[0,1,3],[3,8,5],[9,7,8]]
arr = np.array(x)                     
print("array:")
print(arr)
arr2=np.sort(x)
print("sorted array:")
print(arr2)


# Create a four dimensions array to get the sum over the last two axes at once

# In[15]:


import numpy as np
a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]],[[13,14,15],[16,17,18]]])
print(a)
print("  Sum =",a.sum())


# In[ ]:




