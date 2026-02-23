#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[36]:


df = pd.read_csv('../../data/raw/housing.csv')


# In[37]:


# Missing
(df.isna().sum()/len(df))*100


# In[38]:


df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())


# In[39]:


(df.isna().sum()/len(df))*100


# In[40]:


# Duplicated
df.duplicated().sum()
# df.drop_duplicates()


# In[41]:


# Kiểm tra kiểu dữ liệu
def columns_unique(df):
    result = {}
    for col in df.columns:
        result[col] = df[col].apply(type).unique()
    return result
columns_unique(df)


# In[42]:


# Feature Engineer, biến đổi sau khi chia data vì leak
df['rooms_per_household'] = df['total_rooms'] / df['households']


# In[43]:


df['population_per_household'] = df['population']/df['households']


# In[44]:


df['bedrooms_per_room'] = df['total_bedrooms']/df['total_rooms']


# In[45]:


col = df.pop('median_house_value')
df['median_house_value'] = col
df

# In[47]:


# df['median_house_value'].to_csv('med_house_val.csv')


# In[53]:


threshold = df['median_income'].quantile(0.8) # đã sắp xếp các giá trị từ nhỏ đến lớn và lấy %
df.loc[:,'is_rich'] = (df['median_income'] > threshold).astype(int)


# In[54]:


df


# # In[57]:


# y= df.loc[:,'median_house_value']
# y


# In[61]:


# Split
# num_cols= df.drop(df.columns[[-4,-3]], axis=1)
# x= df.drop('median_house_value', axis=1)
# x


# In[62]:


# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# ct = ColumnTransformer(
#     transformers=
#     [(
#         'encoder', OneHotEncoder(),['ocean_proximity']
#       )],
#     remainder= 'passthrough')

# df_transformed_array = ct.fit_transform(df)
# ohe_cols = ct.named_transformers_['encoder'].get_feature_names_out(['ocean_proximity'])
# other_cols = [c for c in df.columns if c != 'ocean_proximity']
# all_cols = list(ohe_cols) + other_cols

# df_transformed = pd.DataFrame(df_transformed_array, columns=all_cols)
# print(df_transformed)

# # df['ocean_proximity'].unique()
# cat_cols = df.select_dtypes(include=['object','category'])
# cat_cols

df_processed = pd.get_dummies(df,'ocean_proximity')
# dtype= int bỏ
df_processed


# In[25]:

df_processed.to_csv('../../data/processed/df_processed.csv')


# In[26]:


# # Xử lý outlier nếu cần
# columns = df.select_dtypes(include='number').columns
#     # Chọn cột có số nếu không truyền vào cols
# def iqr_outlier_table(df):
#     outlier_table = []
#     # Cách và in bảng tạo list mới tên tuỳ ý
#     for col in columns:
#         Q1 = df[col].quantile(0.25)
#         Q3 = df[col].quantile(0.75)
#         IQR = Q3 - Q1
#         lower = Q1 - 1.5 * IQR
#         upper = Q3 + 1.5 * IQR
        
#         out_low = (df[col] < lower).sum()
        
#         out_high = (df[col] > upper).sum()
#         out_total = out_low + out_high
        
#         outlier_table.append({
#             'column': col,
#             'Q1': Q1.round(3),
#             'Q3': Q3.round(3),
#             'IQR': IQR.round(3),
#             'lower_bound': lower.round(3),
#             'upper_bound': upper.round(3),
#             'out_low': out_low,
#             'out_high': out_high,
#             'out_total': out_total
#         })
    
#     return pd.DataFrame(outlier_table)
# iqr_outlier_table(df)

# # enumerate trả về (index, column_name) cần in không


# In[27]:


# def list_iqr_outliers(df, col):
#     Q1 = df[col].quantile(0.25)
#     Q3 = df[col].quantile(0.75)
#     IQR = Q3 - Q1
#     # Cóp y phần code cần lặp vào và thay tên như thường
#     # Lọc
#     lower = Q1 - 1.5 * IQR
#     upper = Q3 + 1.5 * IQR

#     outliers = df[(df[col] < lower) | (df[col] > upper)].loc[:, [col]]
#     return outliers


# In[28]:


# list_iqr_outliers(df,col="total_rooms").to_csv(
#     "outlier/total_rooms_outliers.csv",
#     index=False
# )


# In[29]:


# list_iqr_outliers(df,col="total_bedrooms").to_csv(
#     "outlier/total_bedrooms_outliers.csv",
#     index=False
# )


# In[30]:


# list_iqr_outliers(df,col="population").to_csv(
#     "outlier/population_outliers.csv",
#     index=False
# )


# In[31]:


# list_iqr_outliers(df,col="households").to_csv(
#     "outlier/households_outliers.csv",
#     index=False
# )


# In[32]:


# list_iqr_outliers(df,col="median_income").to_csv(
#     "outlier/median_income_outliers.csv",
#     index=False
# )


# In[33]:


# list_iqr_outliers(df,col="median_house_value").to_csv(
#     "outlier/median_house_value_outliers.csv",
#     index=False
# )


# In[34]:


# from scipy.stats.mstats import winsorize
# df['household_wins'] = winsorize(df['households'], limits=(0, 0.01))
# df['household_wins'].to_csv('data/hh_wins')


# In[ ]:




