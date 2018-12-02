import numpy as np
from sklearn.datasets import load_iris
from random import random
import math
import operator

irisds = load_iris()
irisds.data.shape

def division(x):
    for i in irisds.data:
        if random() < x:
            train_data.append(i)
        else:
            test_data.append(i)

def euclidean_distance(x, y):
    dist = 0
    for i in range(x.shape[0]):
        dist += math.pow(x[i] - y[i], 2)
    return math.sqrt(dist)

def means(arr):
    sum_ = 0
    for i in arr:
           sum_+=i[feature_val]
    return sum_/len(arr)

def predict(arr, k):
    dist_arr = []
    for i in train_data:
        dist_arr.append((i, euclidean_distance(i, arr)))
    dist_arr.sort(key=operator.itemgetter(1))
    nn = [] 
    for j in range(k):
        nn.append(dist_arr[j][0]) 
    arr[feature_val] = means(nn)
    return arr

train_data = []
test_data = []
feature_val = 0
division(0.90)
for i in test_data:
    print(i)
    print(predict(i, 7))
    print("________________")