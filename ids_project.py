# -*- coding: utf-8 -*-
"""IDS_Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nB7i2cQJmGyMQixjtdQHetunMTzQ2KdR
"""

from google.colab import drive
drive.mount('/content/drive')

# # importing the zipfile module
# from zipfile import ZipFile
  
# # loading the temp.zip and creating a zip object
# with ZipFile("/content/drive/MyDrive/Colab Notebooks/IDS/student.zip", 'r') as zObject:
  
#     # Extracting all the members of the zip 
#     # into a specific location.
#     zObject.extractall(path="/content/drive/MyDrive/Colab Notebooks/IDS/student")

#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

from sklearn.model_selection import train_test_split

df = pd.read_csv("/content/drive/MyDrive/IDS/car/car_data.txt",sep=",",header=None,names=['buying','maint','doors','person','lug_boot','safety','class'])
df

df.isnull().sum()

df.info()

df['doors'].value_counts()

plt.hist(df["class"])
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.title("Distribution of Car Classes")
plt.show()

# Plot a histogram of the buying attribute
plt.hist(df['buying'])
plt.xlabel('Buying')
plt.ylabel('Count')
plt.title('Distribution of Buying Attribute')
plt.show()

# Plot a bar plot of the doors attribute
plt.bar(df['doors'].unique(), df['doors'].value_counts())
plt.xlabel('Doors')
plt.ylabel('Count')
plt.title('Distribution of Doors Attribute')
plt.show()

# Plot a pie chart of the class attribute
plt.pie(df['class'].value_counts(), labels=df['class'].unique())
plt.title('Distribution of Class Attribute')
plt.show()

# Relationship between the price and maintenance cost of the cars
plt.scatter(df['buying'], df['maint'])
plt.xlabel('Buying')
plt.ylabel('Maint')
plt.title('Scatter Plot of Buying vs Maint')
plt.show()

df['doors'] = df['doors'].map({'2':2,'3':3,'4':4,'5more':5}) #Here 5 means 5 or more
df['person'] = df['person'].map({'2':2,'4':4,'more':5}) #Here 5 means 5 or more

df

obj_en = df.select_dtypes("object").columns

def encode(col):
  en_map = {k:v for v,k in enumerate(df[col].unique())}
  df[col] = df[col].map(en_map)
  return en_map

ls_dc = []
for i in obj_en:
  ls_dc.append(encode(i))
ls_dc

df

df.info()

corr_df = df.corr()
plt.figure(figsize = (10, 6))
sns.heatmap(data = corr_df, annot = True)
plt.show()

y = df['class']
 X = df.drop('class',axis=1)

 X

y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 24)

from sklearn.preprocessing import StandardScaler
sc1 = StandardScaler()
sc2 = StandardScaler()
X_train = sc1.fit_transform(X_train)
X_test = sc2.fit_transform(X_test)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,plot_confusion_matrix, precision_score, recall_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.feature_selection import RFE, mutual_info_classif

model1 = LogisticRegression()
model1.fit(X_train, y_train)
y_pred = model1.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="macro")
recall = recall_score(y_test, y_pred, average="macro")

print(f"Accuracy: {accuracy*100}")
print(f"Precision: {precision*100}")
print(f"Recall: {recall*100}")

class_names = [0,1,2,3]
fig, ax = plt.subplots(figsize=(7,3))
plot_confusion_matrix(model1, X_test, y_test,cmap=plt.cm.Reds,labels=class_names,ax=ax,values_format = '.0f')
plt.title('Confusion Matrix')
plt.grid(False)
plt.show()

scores = cross_val_score(model1, X, y, cv=10)

# Plot the results of the cross-validation
plt.bar(range(1, 11), scores)
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.show()

model2 = DecisionTreeClassifier()
model2.fit(X_train, y_train)
y_pred = model2.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="macro")
recall = recall_score(y_test, y_pred, average="macro")

print(f"Accuracy: {accuracy*100}")
print(f"Precision: {precision*100}")
print(f"Recall: {recall*100}")

class_names = [0,1,2,3]
fig, ax = plt.subplots(figsize=(7,3))
plot_confusion_matrix(model2, X_test, y_test,cmap=plt.cm.Reds,labels=class_names,ax=ax,values_format = '.0f')
plt.title('Confusion Matrix')
plt.grid(False)
plt.show()

scores = cross_val_score(model2, X, y, cv=10)

# Plot the results of the cross-validation
plt.bar(range(1, 11), scores)
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.show()

model3 = GaussianNB()
model3.fit(X_train, y_train)
y_pred = model3.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="macro")
recall = recall_score(y_test, y_pred, average="macro")

print(f"Accuracy: {accuracy*100}")
print(f"Precision: {precision*100}")
print(f"Recall: {recall*100}")

class_names = [0,1,2,3]
fig, ax = plt.subplots(figsize=(7,3))
plot_confusion_matrix(model3, X_test, y_test,cmap=plt.cm.Reds,labels=class_names,ax=ax,values_format = '.0f')
plt.title('Confusion Matrix')
plt.grid(False)
plt.show()

scores = cross_val_score(model3, X, y, cv=10)

# Plot the results of the cross-validation
plt.bar(range(1, 11), scores)
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.show()

model4 = RandomForestClassifier()
model4.fit(X_train, y_train)
y_pred = model4.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="macro")
recall = recall_score(y_test, y_pred, average="macro")

print(f"Accuracy: {accuracy*100}")
print(f"Precision: {precision*100}")
print(f"Recall: {recall*100}")

class_names = [0,1,2,3]
fig, ax = plt.subplots(figsize=(7,3))
plot_confusion_matrix(model4, X_test, y_test,cmap=plt.cm.Reds,labels=class_names,ax=ax,values_format = '.0f')
plt.title('Confusion Matrix')
plt.grid(False)
plt.show()

scores = cross_val_score(model4, X, y, cv=10)

# Plot the results of the cross-validation
plt.bar(range(1, 11), scores)
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.show()

model5 = SVC()
model5.fit(X_train, y_train)
y_pred = model5.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="macro")
recall = recall_score(y_test, y_pred, average="macro")

print(f"Accuracy: {accuracy*100}")
print(f"Precision: {precision*100}")
print(f"Recall: {recall*100}")

class_names = [0,1,2,3]
fig, ax = plt.subplots(figsize=(7,3))
plot_confusion_matrix(model5, X_test, y_test,cmap=plt.cm.Reds,labels=class_names,ax=ax,values_format = '.0f')
plt.title('Confusion Matrix')
plt.grid(False)
plt.show()

scores = cross_val_score(model5, X, y, cv=10)

# Plot the results of the cross-validation
plt.bar(range(1, 11), scores)
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.show()

"""Training Model after selecting it

"""

# Tune the model's hyperparameters using grid search
param_grid = {'max_depth': [2, 5, 10, 20, 50], 'min_samples_split': [2, 5, 10, 20]}
grid_search = GridSearchCV(model2, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Print the best hyperparameters and the corresponding mean cross-validated score
print(f'Best hyperparameters: {grid_search.best_params_}')
print(f'Best score: {grid_search.best_score_:.2f}')


# Perform feature selection using recursive feature elimination
selector = RFE(model2, n_features_to_select=5)
selector.fit(X_train, y_train)

# Print the selected features
print(f'Selected features: {df.columns[:-1][selector.support_]}')

# Define the new data to make predictions on
new_data = pd.DataFrame([['vhigh', 'vhigh', '2', '2', 'small', 'low', 'unacc'],
                         ['high', 'high', '4', 'more', 'big', 'high', 'acc'],
                         ['low', 'low', '3', '2', 'med', 'med', 'good']])

# Encode the categorical features of the new data using one-hot encoding
new_data = pd.get_dummies(new_data, columns=[0, 1, 2, 3, 4, 5])

# Use the model to predict the labels for the new data
new_data_pred = model2.predict(new_data)

# Print the predictions
print(f'Predictions: {new_data_pred}')