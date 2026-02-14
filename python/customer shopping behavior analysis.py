#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd 

df= pd.read_csv('customer_shopping_behavior.csv')


# In[7]:


df.head()


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


df.describe(include='all')


# In[11]:


df.isnull().sum()


# In[12]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))


# In[13]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[14]:


df.columns


# In[15]:


#create a column age_group
labels =['Young Adult', 'Adult', 'Middle-aged','Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels )


# In[16]:


df[['age','age_group']].head(10)


# In[17]:


# create column purchase_frequency_days

frequency_mapping ={
    'Fornightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[18]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[19]:


df[['discount_applied','promo_code_used']].head(10)


# In[20]:


(df['discount_applied'] == df['promo_code_used']).all()


# In[21]:


df = df.drop('promo_code_used', axis=1)


# In[22]:


df.columns


# In[1]:


get_ipython().system('python -m pip install --upgrade pip --user')


# In[2]:


get_ipython().system('pip install --user --only-binary :all: psycopg2-binary==2.9.9 sqlalchemy')


# In[4]:


import sys
import site
user_site = site.getusersitepackages()
if user_site not in sys.path:
    sys.path.append(user_site)
print(f"Added: {user_site}")


# In[5]:


import psycopg2
import sqlalchemy
print(f"psycopg2: {psycopg2.__version__}")
print(f"sqlalchemy: {sqlalchemy.__version__}")
print("✅ Success!")


# In[26]:


# Step 0: Import required libraries
from sqlalchemy import create_engine
import pandas as pd

# Step 1: Connect to PostgreSQL
username = "postgres"  # default user
password = "Ln@jy" # the password you set during installation
host = "localhost" # if running locally
port = "5432" # default PostgreSQL port
database = "customer_behavior" # the database you created in pgAdmin

# Also fix typo: postgresq1 → postgresql
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Step 2: Load DataFrame into PostgreSQL
table_name = "customer" # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")


# In[ ]:




