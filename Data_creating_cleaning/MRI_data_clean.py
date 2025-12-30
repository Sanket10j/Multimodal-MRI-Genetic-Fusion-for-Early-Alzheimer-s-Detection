#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import os
import shutil


# In[2]:


input_path = r'Processed_gene_mri_subject_id.csv'


# In[3]:


df = pd.read_csv(input_path)


# In[4]:


df.head(), df.columns.tolist()


# In[9]:


#df = df.dropna(columns=['n','IID','a','b','c','d'])
df = df.drop(columns=["n", "IID", "a", "b", "c", "d"])


# In[10]:


df


# In[11]:


ds = pd.read_csv(r"D:\Downloads\genotype_embeddings_64_ED.csv")


# In[12]:


ds


# In[14]:


iids = ds.pop("IID").tolist()


# In[18]:


iids


# In[19]:


filtered_df = df[df["subject_id"].isin(iids)].copy()


# In[20]:


filtered_df


# In[23]:


um_unique_subjects = filtered_df["subject_id"].nunique()


# In[24]:


um_unique_subjects


# In[25]:


unique_df = filtered_df.drop_duplicates(subset=["subject_id"], keep="first")


# In[26]:


unique_df


# In[27]:


unique_df.to_csv("filtered_by_subject_id_ffffffffff.csv", index=False)


# In[29]:


# subject IDs for DXNORM
dxnorm_ids = unique_df.loc[unique_df["DXNORM"] == 1, "subject_id"].tolist()

# subject IDs for DXMCI
dxmci_ids = unique_df.loc[unique_df["DXMCI"] == 1, "subject_id"].tolist()

# subject IDs for DXAD
dxad_ids = unique_df.loc[unique_df["DXAD"] == 1, "subject_id"].tolist()


# In[33]:


len(dxnorm_ids), len(dxmci_ids), len(dxad_ids)


# In[35]:


dxnorm_path = 'D:\BAPS\Projects\mmil\ADNI1_T1w_Normal_at_m12_MRI\ADNI'
dxmci_path = "D:\BAPS\Projects\mmil\ADNI1_T1w_DXMCI=1_at_m18_MRI\ADNI"
dxad_path  = "D:\BAPS\Projects\mmil\ADNI1_T1w_Cohort_AD_Visit_12_MRI\ADNI"


# In[36]:


def clean_class_folder(folder_path, allowed_ids):
    for subject_folder in os.listdir(folder_path):
        subject_path = os.path.join(folder_path, subject_folder)
        if os.path.isdir(subject_path):  # make sure it's a folder
            if subject_folder not in allowed_ids:
                shutil.rmtree(subject_path)


# In[38]:


clean_class_folder(dxnorm_path, dxnorm_ids)
clean_class_folder(dxmci_path, dxmci_ids)
clean_class_folder(dxad_path, dxad_ids)


# In[ ]:




