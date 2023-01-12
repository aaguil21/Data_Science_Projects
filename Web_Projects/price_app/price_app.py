import pandas as pd
df = pd.read_csv('prices.csv')

y =  df['Value']
X = df.drop('Value', axis=1)

from sklearn import linear_model

lm = linear_model.LinearRegression()
lm.fit(X, y)

import pickle
pickle.dump(lm, open('model.pkl', 'wb'))