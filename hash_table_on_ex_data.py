#!/usr/bin/env python
# coding: utf-8

# In[23]:


from hash_test import Node
from hash_test import HashTable
import pandas as pd
import numpy as np
df = pd.read_excel("COMPLETED_v3sequestration_data_example.xlsx")
img_ids = list(df["submitter_id"])
h = HashTable()
h.init_table(img_ids)
try:
    numsamp = int(input("Number of samples: "))
    ssize = int(input("Sample Size: "))
except Exception:
    print("Invalid Input")
for s_id in range(1,numsamp+1):
    samp = np.random.choice(img_ids, ssize)
    for img in samp:
        h.insert(s_id,img,img_ids)
h.print_hash()


# ##### 
