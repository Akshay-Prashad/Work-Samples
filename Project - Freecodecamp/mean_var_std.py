#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[83]:


def calculate(a):
    if len(a)==9:
        n=np.array(a)
        p=n.reshape((3,3))
        dit_mean_var_sd={"mean":[list(np.mean(p,axis=0)),list(np.mean(p,axis=1)),float(np.mean(n))],
                        "variance":[list(np.var(p,axis=0)),list(np.var(p,axis=1)),float(np.var(n))],
                        "standard deviation":[list(np.std(p,axis=0)),list(np.std(p,axis=1)),float(np.std(n))],
                        "max":[list(np.max(p,axis=0)),list(np.max(p,axis=1)),int(np.max(n))],
                        "min":[list(np.min(p,axis=0)),list(np.min(p,axis=1)),int(np.min(n))],
                        "sum":[list(np.sum(p,axis=0)),list(np.sum(p,axis=1)),int(np.sum(n))],}
        return  dit_mean_var_sd
    else:
        raise Exception("List must contain nine numbers.")
        return
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




