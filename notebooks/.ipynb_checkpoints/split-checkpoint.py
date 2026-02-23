#!/usr/bin/env python
# coding: utf-8

# In[1]:


import feature as fe


# In[2]:


x = fe.x
y = fe.y
x


# In[15]:


x.columns = x.columns.str.replace(r"[\[\]<>?]", "_", regex=True)
x.columns = [c.replace(" ", "_") for c in x.columns]
x


# In[10]:


y


# In[ ]:


# Sử dụng cho lần sau RandomizedSearchCV 
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def evaluation_model(models,x,y, cv=5):
    result={}
    for name, model in models.items():
        # item trả về key, value
        scores = cross_val_score(model,x,y, cv=cv)
        result[name] = scores.mean()
        # Cách gọi value = Ghi đè key lên
    return result

models= {
    'lr': LinearRegression(),
    'ridge': make_pipeline(StandardScaler(),Ridge(max_iter=10_000)),
    'lasso': make_pipeline(StandardScaler(),Lasso(max_iter=10_000)),
    'elasnet': make_pipeline(StandardScaler(),ElasticNet(max_iter=10_000)),
    'dtree': DecisionTreeRegressor(),
    'rf':RandomForestRegressor(),
    'gbr':GradientBoostingRegressor(),
    'xg':XGBRegressor(),
    'lgbm':LGBMRegressor(verbose=-1),
    'cb':CatBoostRegressor(verbose=0)
    # Input để giới hạn log
}
evaluation_model(models, x, y)

# Chỉ 3 cái cần max_iter: Ridge – Lasso – ElasticNet là có vòng lặp nên cần thêm max_iter(max vòng lặp)

# Chạy lâu => lưu lại giá trị
# {'lr': np.float64(0.5648146578479464),
#  'ridge': np.float64(0.5648029739840332),
#  'lasso': np.float64(0.5648384235220549),
#  'elasnet': np.float64(0.46635582314366425),
#  'dtree': np.float64(0.2584905175729153),
#  'rf': np.float64(0.6017418960503296),
#  'gbr': np.float64(0.6508721307495218),
#  'xg': np.float64(0.6446990090095659),
#  'lgbm': np.float64(0.6713053936078819),
#  'cb': np.float64(0.6954852523946173)}


# In[16]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =0.2, random_state = 42)
x_train.info()


# In[17]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
num_cols = x_train.select_dtypes(include=['int64','float64']).columns
x_train[num_cols] = scaler.fit_transform(x_train[num_cols] )
x_test[num_cols] = scaler.transform(x_test[num_cols])
x_train
# x_train[ ]= scaler.fit_transform(x_train)
# x_test = 

