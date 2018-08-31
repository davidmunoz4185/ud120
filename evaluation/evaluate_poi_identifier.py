#!/usr/bin/python

from __future__ import division

"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here

from sklearn import cross_validation
from sklearn import tree
from sklearn import metrics

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels,  test_size = 0.3, random_state = 42)

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test, labels_test)

print metrics.accuracy_score(labels_test, pred)

pred = clf.predict(features_test)
print metrics.precision_score(labels_test, pred)
print metrics.recall_score(labels_test, pred)

"""
print precision_score(y_test, y_pred, average='macro') 
print recall_score(y_test, y_pred, average='macro')
"""

count = 0
print labels_test
for i in labels_test:
    if i == 1.0:
        count +=1
print count
print len(labels_test)



from sklearn import cross_validation
from sklearn import tree
x_train,x_test, y_train,y_test=cross_validation.train_test_split(features,labels)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
print precision_score(y_test, y_pred)
print recall_score(y_test, y_pred)

from time import time
from sklearn import cross_validation
from sklearn import tree
from sklearn.metrics import accuracy_score

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)


print labels_test

count =0
for i in range(0, len(labels_test)):
    if labels_test[i] == 1.0:
        count += 1

print ("Total number of records in labels_test= ",len(labels_test))
print ("Total number of POIs (where poi = 1)= ",count)

total_labels_test = len(labels_test)
total_POI = count

t0 = time()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)


print ("training time: ", round(time() - t0,3), "s")

t0 = time()
pred = clf.predict(features_test)

print ("predict time: ", round(time() - t0,3), "s")
print ("prediction= ", pred)

accuracy = accuracy_score(pred, labels_test)
print ("accuracy [overfit full dataset]= ",accuracy)


mytest = float((total_labels_test-total_POI)/total_labels_test)
print total_labels_test-total_POI, total_labels_test, ((total_labels_test-total_POI)/total_labels_test)
print (mytest)

print ("'Precision= ",precision_score(labels_test, pred, average='macro'))
print ("'Recall= ", recall_score(labels_test, pred, average='macro'))



print ("'Precision= ",precision_score(labels_test, pred, average='macro'))
print ("'Recall= ", recall_score(labels_test, pred, average='macro'))
print ("'Precision= ",precision_score(labels_test, pred))
print ("'Recall= ", recall_score(labels_test, pred))


from sklearn.metrics import accuracy_score, recall_score, precision_score, classification_report

print ("'Precision (macro)= ",precision_score(labels_test, pred, average='macro'))
print ("'Recall (macro)= ", recall_score(labels_test, pred, average='macro'))
print ("'Precision (None)= ",precision_score(labels_test, pred, average=None))
print ("'Recall (None)= ", recall_score(labels_test, pred, average=None))
print ("'Precision (micro)= ",precision_score(labels_test, pred, average='micro'))
print ("'Recall (micro)= ", recall_score(labels_test, pred, average='micro'))
print ("'Precision (default)= ",precision_score(labels_test, pred))
print ("'Recall (default)= ", recall_score(labels_test, pred))


print("Classification Report: \n")
print(classification_report(pred, labels_test))