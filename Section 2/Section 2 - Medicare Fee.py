#!/usr/bin/env python
# coding: utf-8

# In[203]:


import numpy as np
import pandas as pd


# ### Importing Data

# In[208]:


df17 = pd.read_table("PartD_Prescriber_PUF_NPI_17.txt", header = None)


# In[209]:


new_header = df17.iloc[0] 
df17 = df17[1:] 
df17.columns = new_header


# ### Question 1

# In[210]:


df17['bene_count'] = df17['bene_count'].apply(pd.to_numeric, downcast='float', errors='coerce')


# In[213]:


dftenplusben=df17[df17['bene_count']>10]


# In[214]:


dftenplusben['bene_count'].mean()


# ### Question 2

# In[215]:


df17['total_day_supply'] = df17['total_day_supply'].apply(pd.to_numeric, downcast='float', errors='coerce')
df17['total_claim_count'] = df17['total_claim_count'].apply(pd.to_numeric, downcast='float', errors='coerce')


# In[216]:


df17['len_avg_prsc'] = df17['total_day_supply']/df17['total_claim_count']


# In[217]:


df17['len_avg_prsc'].median()


# ### Question 3

# In[218]:


df17['total_claim_count'] = df17['total_claim_count'].apply(pd.to_numeric, downcast='float', errors='coerce')
df17['brand_claim_count'] = df17['brand_claim_count'].apply(pd.to_numeric, downcast='float', errors='coerce')


# In[219]:


ttl_brnd_spc=df17[['total_claim_count','brand_claim_count','specialty_description']]


# In[220]:


ttl_brnd_spc = ttl_brnd_spc.dropna()


# In[221]:


avg_total_claim_by_spc = ttl_brnd_spc.groupby('specialty_description')['total_claim_count'].mean()


# In[222]:


avg_brand_claim_by_spc = ttl_brnd_spc.groupby('specialty_description')['brand_claim_count'].mean()


# In[223]:


merged = pd.merge(avg_brand_claim_by_spc,avg_total_claim_by_spc,how='left', on='specialty_description')


# In[224]:


ratio = merged[merged['total_claim_count']>1000]


# In[225]:


rat = ratio['brand_claim_count']/ratio['total_claim_count']


# In[226]:


np.std(rat)


# ### Question 4

# In[227]:


df17['opioid_bene_count'] = df17['opioid_bene_count'].apply(pd.to_numeric, downcast='float', errors='coerce')
df17['antibiotic_bene_count'] = df17['antibiotic_bene_count'].apply(pd.to_numeric, downcast='float', errors='coerce')


# In[228]:


grouped_by_state = df17.groupby('nppes_provider_state').apply(lambda x: x['opioid_bene_count'].sum()/x['antibiotic_bene_count'].sum())


# In[229]:


grouped_by_state.dropna().max()-grouped_by_state.dropna().min()


# ### Question 5

# In[231]:


df17['total_claim_count_ge65'] = df17['total_claim_count_ge65'].apply(pd.to_numeric, downcast='float', errors='coerce')
df17['lis_claim_count'] = df17['lis_claim_count'].apply(pd.to_numeric, downcast='float', errors='coerce')


# In[232]:


lis_ge65 = df17[['total_claim_count_ge65','lis_claim_count']]


# In[233]:


lis_ge65 = lis_ge65.dropna()


# In[234]:


lis_ge65['total_claim_count_ge65'].corr(lis_ge65['lis_claim_count'], method ='pearson')


# ### Question 6

# In[235]:


df17['opioid_day_supply'] = df17['opioid_day_supply'].apply(pd.to_numeric, downcast='float', errors='coerce')
df17['opioid_claim_count'] = df17['opioid_claim_count'].apply(pd.to_numeric, downcast='float', errors='coerce')


# In[236]:


df17['opi_avg_len'] = df17['opioid_day_supply']/df17['opioid_claim_count']


# In[237]:


st_sp_pair = pd.pivot_table(df17,index = 'nppes_provider_state',values = 'opi_avg_len', columns ='specialty_description')


# In[238]:


st_sp_pair_t = st_sp_pair.transpose()
st_sp_pair_t['national_avg'] = st_sp_pair_t.sum(axis=1)/61


# In[239]:


max_rat_st=st_sp_pair_t.fillna(0).div(st_sp_pair_t['national_avg'],axis = 0).max()


# In[240]:


max_rat_st.max()


# ### Question 7

# In[241]:


df16 = pd.read_table("PartD_Prescriber_PUF_NPI_16.txt", header = None)


# In[242]:


new_header = df16.iloc[0] 
df16 = df16[1:] 
df16.columns = new_header


# In[243]:


df17['total_drug_cost'] = df17['total_drug_cost'].apply(pd.to_numeric, downcast='float', errors='coerce')
df17['total_day_supply'] = df17['total_day_supply'].apply(pd.to_numeric, downcast='float', errors='coerce')
df16['total_drug_cost'] = df16['total_drug_cost'].apply(pd.to_numeric, downcast='float', errors='coerce')
df16['total_day_supply'] = df16['total_day_supply'].apply(pd.to_numeric, downcast='float', errors='coerce')


# In[244]:


df17['avg_cost_per_day']=df17['total_drug_cost']/df17['total_day_supply']
df17_inf=df17[['npi','avg_cost_per_day']]


# In[245]:


df16['avg_cost_per_day']=df16['total_drug_cost']/df16['total_day_supply']
df16_inf=df16[['npi','avg_cost_per_day']]


# In[246]:


merged=pd.merge(df16_inf,df17_inf,how='left',on='npi')


# In[247]:


inf = (merged['avg_cost_per_day_y']-merged['avg_cost_per_day_x'])/merged['avg_cost_per_day_x']


# In[248]:


inf.mean()


# ### Question 8

# In[376]:


def_spc16 = df16[['npi','specialty_description']]


# In[377]:


def_spc17 = df17[['npi','specialty_description']]


# In[378]:


merged=pd.merge(def_spc16,def_spc17,how='left',on ='npi')


# In[379]:


npi_by_spc16=merged.groupby('specialty_description_x')['npi'].count()


# In[380]:


npi_by_spc16=pd.Series.to_frame(npi_by_spc16)


# In[381]:


npi_by_spc16=npi_by_spc16.reset_index()


# In[382]:


npi_by_spc16= npi_by_spc16.rename(columns={'specialty_description_x': 'spc'})


# In[383]:


npi_by_spc17=merged.groupby('specialty_description_y')['npi'].count()


# In[384]:


npi_by_spc17=pd.Series.to_frame(npi_by_spc17)


# In[385]:


npi_by_spc17=npi_by_spc17.reset_index()


# In[388]:


npi_by_spc17= npi_by_spc17.rename(columns={'specialty_description_y': 'spc'})


# In[389]:


merged2=pd.merge(npi_by_spc16,npi_by_spc17,how='left',on='spc')


# In[392]:


ratio=(merged2['npi_y']-merged2['npi_x'])/merged2['npi_x']


# In[397]:


ratio.min()

