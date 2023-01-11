# -*- coding: utf-8 -*-
"""
Created on Wed mar 14 19:03:21 2021

@author: rahul
"""
import csv
import numpy as np 
import pandas as pd 
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.tree import export_graphviz
data=pd.read_csv("finalfever.csv")
print(data.head())

data_inputs=data[["age","temperature","cold"]]
print(data_inputs.head())
expected_output=data[["medicine"]]
print(expected_output.head())

data_inputs["temperature"].replace(['102','103','104','105','106'],2,inplace=True)
data_inputs["temperature"].replace(['100','101'],1,inplace=True)
data_inputs["temperature"].replace(['97','98','99'],0,inplace=True)
print(data_inputs.head())


data_inputs["age"].replace("young",0,inplace=True)
data_inputs["age"].replace("middle",1,inplace=True)
data_inputs["age"].replace("adult",2,inplace=True)
print(data_inputs.head())




data_inputs["cold"].replace("yes",1,inplace=True)
data_inputs["cold"].replace("no",0,inplace=True)
print(data_inputs.head())


expected_output["medicine"].replace("dola",0,inplace=True)
expected_output["medicine"].replace("dola&amoxzylin",1,inplace=True)
expected_output["medicine"].replace("crocin",2,inplace=True)
expected_output["medicine"].replace("paracetamol",3,inplace=True)
expected_output["medicine"].replace("electrolyte",4,inplace=True)
expected_output["medicine"].replace("acetaminophen&phenylephrine",5,inplace=True)
expected_output["medicine"].replace("ibuprofen",6,inplace=True)
expected_output["medicine"].replace("phenylephrine",7,inplace=True)
expected_output["medicine"].replace("acetaminophen",8,inplace=True)


print(expected_output.head())


X_train,X_test,Y_train,Y_test=train_test_split(data_inputs,expected_output,test_size=0.2,random_state=100)
tree1 = tree.DecisionTreeClassifier(max_depth = 3, min_samples_split = 2)
tree1.fit(X_train,Y_train)

accuracy=tree1.score(X_test,Y_test)
print("Accuracy={}%".format(accuracy*100))


def predict_medicine(name,gender,age,temperature,cold):
    myFile = open('patientdatabase.csv', 'w')  
    with myFile:  
        myFields = ['name','gender', 'age','temperature','cold']
        writer = csv.DictWriter(myFile, fieldnames=myFields)    
        writer.writeheader()
        writer.writerow({'name':name,'gender':gender, 'age':age,'temperature':temperature,'cold':cold })
    Xnew = [[age,temperature,cold]]   
    test=tree1.predict(Xnew)
    print("The prescribed medicine is")
    if test==0:
        medicine="Dola-650"
    elif test==1:
        medicine="Dola-650 & Amoxzylin"
    elif test==2:
        medicine="Crocin"
    elif test==3:
        medicine="Paracetamol"   
    elif test==4:
        medicine="Electrolyte"
    elif test==5:
        medicine="Acetaminophen & Phenylephrine"
    elif test==6:
        medicine="Ibuprofen"   
    elif test==7:
        medicine="Phenylephrine"
    else:
        medicine="Acetaminophen"    
     
    return medicine


         
    
joblib.dump(tree1,'feverGUI.pkl')
