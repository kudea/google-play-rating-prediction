import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import svm
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import tkinter as tk



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
y = df['Rating'].astype(int)


#spite for train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 10)

svm = svm.SVR()
svm.fit(X_train, y_train)
accuracy = svm.score(X_test,y_test)
print('Accuracy: ' + str(np.round(accuracy*100, 2)) + '%')  




window = tk.Tk()
window.title('Predict Rate App')
window.geometry('800x350')
window.configure(background='gray')


def calculate_number():

    df['Size'] = size_entry.get()
    df['Type'] = type_entry.get()
    df['Price'] = prize_entry.get()
    df['Content Rating'] = cr_entry.get()
    df['Genres'] = g_entry.get()
    
    
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
    
    features = ['Size','Type', 'Price', 'Content Rating', 'Genres']
    Xp = df[features]
    rating_value = svm.predict(Xp)
    r_value = list(set(rating_value))
    r = r_value[0]
    result = 'Your Rating may be：{} \n {}'.format(r, status_description(r))
    # 將計算結果更新到 result_label 文字內容
    result_label.configure(text=result)
    
    
def status_description(r):
    
    if r < 2:
        return 'Maybe you should design another new app, do not give up !'
    elif r >= 2 and r < 4:
        return 'Improve your idea more, and you may desigh a better app .'
    elif r >= 4 :
        return 'Wow ! It is a fantasy app, wish you become the hottest seller !'
    
Paid = {'Free':0,'Paid':1}

header_label = tk.Label(window, text='Google Play app rating Predictor', font = 'Helvetica -40 bold')
header_label.pack()


size_frame = tk.Frame(window)
# 向上對齊父元件
size_frame.pack(side=tk.TOP)
size_label = tk.Label(size_frame, text='Size', font = 'Helvetica -20 bold')
size_label.pack(side=tk.LEFT)
size_entry = tk.Entry(size_frame, font = 'Helvetica -20 bold')
size_entry.pack(side=tk.LEFT)


type_frame = tk.Frame(window)
type_frame.pack(side=tk.TOP)
type_label = tk.Label(type_frame, text='Type', font = 'Helvetica -20 bold')
type_label.pack(side=tk.LEFT)
type_entry = tk.Entry(type_frame, font = 'Helvetica -20 bold')
type_entry.pack(side=tk.LEFT)

prize_frame = tk.Frame(window)
prize_frame.pack(side=tk.TOP)
prize_label = tk.Label(prize_frame, text='Prize', font = 'Helvetica -20 bold')
prize_label.pack(side=tk.LEFT)
prize_entry = tk.Entry(prize_frame, font = 'Helvetica -20 bold')
prize_entry.pack(side=tk.LEFT)

cr_frame = tk.Frame(window)
cr_frame.pack(side=tk.TOP)
cr_label = tk.Label(cr_frame, text='Content rating', font = 'Helvetica -20 bold')
cr_label.pack(side=tk.LEFT)
cr_entry = tk.Entry(cr_frame, font = 'Helvetica -20 bold')
cr_entry.pack(side=tk.LEFT)

g_frame = tk.Frame(window)
g_frame.pack(side=tk.TOP)
g_label = tk.Label(g_frame, text='Genres', font = 'Helvetica -20 bold')
g_label.pack(side=tk.LEFT)
g_entry = tk.Entry(g_frame, font = 'Helvetica -20 bold')
g_entry.pack(side=tk.LEFT)

result_label = tk.Label(window, font = 'Helvetica -16 bold')
result_label.pack()

calculate_btn = tk.Button(window, text='Predict', font = 'Helvetica -20 bold', command=calculate_number)
calculate_btn.pack()

window.mainloop()
