#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
list = enron_data.keys()
print list
print len(list)
print len(enron_data['METTS MARK'].keys())

count = 0
for person in enron_data:
    if enron_data[person]["poi"] == 1:
        count = count + 1

print count

print enron_data['PRENTICE JAMES'].keys()

print enron_data['PRENTICE JAMES']['total_stock_value']

print enron_data['COLWELL WESLEY'].keys()

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print enron_data['SKILLING JEFFREY K'].keys()

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "FASTOW ANDREW S"
print enron_data['FASTOW ANDREW S']['total_payments']

print "LAY KENNETH L"
print enron_data['LAY KENNETH L']['total_payments']

print "SKILLING JEFFREY K"
print enron_data['SKILLING JEFFREY K']['total_payments']

"""for guy in enron_data:
    for x in enron_data[guy]:
        print guy
        print x
        print enron_data[guy][x]
"""

count = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
for guy in enron_data:
    #print guy
    #print enron_data[guy]['salary']
    if enron_data[guy]['email_address'] != "NaN": count2 += 1
    if enron_data[guy]['salary'] != "NaN": count += 1
    if enron_data[guy]['total_stock_value'] == "NaN": count3 += 1
    if enron_data[guy]['total_payments'] == "NaN" and enron_data[guy]['poi'] == "True": count5 += 1
    if enron_data[guy]['poi'] == "True": count6 = count6 + 1
    if enron_data[guy]['poi']: count6 += 1
    count4 += 1

print count
print count2
print count3
print count4
print count3 / count4
print count5
print count6