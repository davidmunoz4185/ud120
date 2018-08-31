#!/usr/bin/python

import pickle
import sys
import re
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
l_salary = []
key = "TOTAL"
data_dict.pop(key, 0)
for key in data_dict.keys():
    #print key, data_dict[key]['salary'], data_dict[key]['bonus']
    if data_dict[key]['salary'] >= 26704229: print key
    if data_dict[key]['salary']!="NaN" and data_dict[key]['salary'] < 26704229: l_salary.append(data_dict[key]['salary'])
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
print max(l_salary)

list = []
### your code below
for point in data:
    salary = point[0]
    list.append(salary)
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
print max(list)



