# -*- coding: utf-8 -*-
"""Sign Language Prediction - Multinomial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wAJhqCFJhPye7a4IX5-DVXXPufxWVChE
"""

from google.colab import drive
drive.mount('/content/drive')

cd /content/drive/MyDrive/Logistic_Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string
import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")

Train_df = pd.read_csv('sign_mnist_train.csv')
Test_df = pd.read_csv('sign_mnist_test.csv')

Train_df.columns.values

Train_df.head()



print(sorted(Train_df["label"].unique()))

print(Train_df.shape[1])

numlist = []
for i in range(26):
  numlist.append(i)

print(numlist)

letters = dict(enumerate(string.ascii_uppercase))
print(letters)

print(sorted(Test_df["label"].unique()))

def dataframe_to_array(dataframe):
  dataframe1 = dataframe.copy(deep = True)
  input_array = dataframe1.iloc[:,1:].to_numpy()
  output_array = dataframe1['label'].to_numpy()
  return input_array, output_array

Train_input_array, Train_output_array = dataframe_to_array(Train_df)
Test_input_array, Test_output_array = dataframe_to_array(Test_df)
print(Train_input_array)

print(Train_output_array)

print(Train_input_array.shape)

pic1 = np.reshape(Train_input_array[0], (28,28))
print(pic1.shape)
plt.imshow(pic1)

plt.imshow(pic1, cmap = "gray")
print("Letter: ", letters[Train_output_array[0].item()])

rows_for_plot = 3
columns_for_plot = 3

pic1 = np.reshape(Train_input_array[0], (28, 28))
plt.subplot(rows_for_plot, columns_for_plot, 1)
plt.imshow(pic1)
plt.title(letters[Train_output_array[0].item()])

plt.subplot(rows_for_plot, columns_for_plot, 2)
pics1 = np.reshape(Train_input_array[0], (28,28))
plt.imshow(pic1, cmap = "rainbow")
plt.title(letters[Train_output_array[0].item()])

plt.tight_layout(pad=1.0)

pic1 = np.reshape(Train_input_array[1], (28, 28))
plt.subplot(rows_for_plot, columns_for_plot, 3)
plt.imshow(pic1)
plt.title(letters[Train_output_array[1].item()])

plt.subplot(rows_for_plot, columns_for_plot, 4)
pics1 = np.reshape(Train_input_array[1], (28,28))
plt.imshow(pic1, cmap = "autumn")
plt.title(letters[Train_output_array[1].item()])

plt.tight_layout(pad=1.0)

pic1 = np.reshape(Train_input_array[0], (28, 28))
plt.subplot(rows_for_plot, columns_for_plot, 5)
plt.imshow(pic1)
plt.title(letters[Train_output_array[0].item()])

plt.subplot(rows_for_plot, columns_for_plot, 6)
pics1 = np.reshape(Train_input_array[0], (28,28))
plt.imshow(pic1, cmap = "spring")
plt.title(letters[Train_output_array[0].item()])

plt.tight_layout(pad=1.0)

print(Train_df[Train_df["label"] == 1].index.values)

for plot_num in range(20):
  if (plot_num % 5 == 0):
    print(plot_num)

rows_for_plot = 6
columns_for_plot = 5
label_list = Train_df["label"].values
plot_num = 0

for i in range(0, 26):
  if i in label_list:
    index = Train_df[Train_df["label"] == i].index.values[0]
    print("Label number:", i, "Letter", letters[Train_output_array[index].item()], "index", index)

    plot_num += 1

    plt.subplot(rows_for_plot, columns_for_plot, plot_num)

    pic1 = np.reshape(Train_input_array[index], (28, 28))
    plt.axis("off")
    plt.imshow(pic1, cmap = "gray")
    plt.title(letters[Train_output_array[index].item()])

    if (plot_num % 5 == 0):
      plt.tight_layout(pad = 1.0)
    else:
      plt.tight_layout(pad = 0.0)

X = Train_input_array.copy()
Y = Train_output_array.copy()
X_test = Test_input_array.copy()
Y_test = Test_output_array.copy()

X_train, X_val, Y_train, Y_val = train_test_split(X, Y, random_state = 42, stratify = Y, test_size = 0.2)
print(f"Shape of X train: {X_train.shape} \nShape of y train: {Y_train.shape}")
print(f"Shape of X train: {X_val.shape} \nShape of Y val: {Y_val.shape}")

train_samples, n_features = X_train.shape
n_classes = np.unique(Y).shape[0]
print("Number of training samples:", train_samples)
print("Number of feature in each sample:", n_features)
print("Number of class:", n_classes)

log_reg_model = LogisticRegression(solver = "lbfgs", multi_class = "multinomial", max_iter = 20)
log_reg_model.fit(X_train, Y_train)

Y_pred = log_reg_model.predict(X_val)
print("=========Classification report=======")
print(classification_report(Y_val, Y_pred))

print(letters)
print(letters[0])
Y_pred = log_reg_model.predict(X_test)

print("In Test Dataset, Total Number of Images:", len(Y_pred))
print("Preduction of number of images for each label")

for i in range(len(letters)):
  print(letters[i], sum(Y_pred == i))

print("=========Classification report=======")
print(classification_report(Y_test, Y_pred))

index = 1000
img = X_test[index]
actual_label = Y_test[index]
predicted_label = Y_pred[index]

print("Actual Letter: ", letters[actual_label.item()])
print("Predicted Letter: ", letters[predicted_label.item()])

plt.imshow(img.reshape((28,28)), cmap = "gray")

index = 500
img = X_test[index]
actual_label = Y_test[index]
predicted_label = Y_pred[index]

print("Actual Letter: ", letters[actual_label.item()])
print("Predicted Letter: ", letters[predicted_label.item()])

plt.imshow(img.reshape((28,28)), cmap = "gray")

from sklearn.model_selection import learning_curve
train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(LogisticRegression(solver='lbfgs', multi_class = "multinomial", max_iter = 20), X, Y,  cv=2, n_jobs=1, scoring="accuracy", return_times=True)

test_scores_mean = np.mean(test_scores, axis = 1)
fit_times_mean = np.mean(fit_times, axis = 1)

fit_time_argsort = fit_times_mean.argsort()
fit_time_sorted = fit_times_mean[fit_time_argsort]
test_scores_mean_sorted = test_scores_mean
plt.plot(fit_time_sorted, test_scores_mean_sorted, "*-")
plt.xlabel("Model Training Time in Seconds")
plt.ylabel("Scores")
plt.title("Performance Curve")
plt.show()