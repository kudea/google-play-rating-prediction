import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv('googleplaystore.csv')

#data preprocessing
i = df[df['Category'] == '1.9'].index
df.loc[i]
df = df.drop(i)
df = df[pd.notnull(df['Rating'])]
df = df[pd.notnull(df['Price'])]
df = df[pd.notnull(df['Size'])]
df = df[pd.notnull(df['Type'])]
df = df[pd.notnull(df['Content Rating'])]
df = df[pd.notnull(df['Genres'])]

#encoding
le = preprocessing.LabelEncoder()
df['Type'] = pd.get_dummies(df['Type'])
df['Price'] = df['Price'].apply(lambda x : x.strip('$'))
df['Content Rating'] = le.fit_transform(df['Content Rating'])
df['Genres'] = le.fit_transform(df['Genres'])
#deal with 'size'
k_indices = df['Size'].loc[df['Size'].str.contains('k')].index.tolist()
converter = pd.DataFrame(df.loc[k_indices, 'Size'].apply(lambda x: x.strip('k')).astype(float).apply(lambda x: x / 1024).apply(lambda x: round(x, 3)).astype(str))
df.loc[k_indices,'Size'] = converter
df['Size'] = df['Size'].apply(lambda x: x.strip('M'))
df[df['Size'] == 'Varies with device'] = 0
df['Size'] = df['Size'].astype(float)

#take specific attributes
features = ['Size','Type', 'Price', 'Content Rating', 'Genres']
X = df[features]
y = df['Rating'].astype(float)

#spite for train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 10)

model = KNeighborsRegressor(n_neighbors=15)
model.fit(X_train, y_train)
accuracy = model.score(X_test,y_test)
print('Accuracy: ' + str(np.round(accuracy*100, 2)) + '%')  