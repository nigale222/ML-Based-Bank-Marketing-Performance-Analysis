import config
import json
import pickle
import numpy as np

import warnings as w
w.filterwarnings("ignore")

class Term_deposit():
    def __init__(self,age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous):   
        
        self.age                    = age
        self.job                    = job
        self.marital                = marital
        self.education              = education 
        self.default                = default
        self.balance                = balance
        self.housing                = housing
        self.loan                   = loan 
        self.contact                = contact
        self.day                    = day
        self.month                  = month
        self.duration               = duration
        self.campaign               = campaign
        self.pdays                  = pdays
        self.previous               = previous
        

    def get_model(self):
        with open(config.Lable_file,"r") as f:
            self.lable = json.load(f)

        with open(config.Model_file,"rb") as file:
            self.model = pickle.load(file)  

    def get_prediction(self):
        self.get_model() 
        array = np.arange(0,len(self.lable["columns"]),dtype=int)

        array[0] = self.age
        array[1] = self.lable["job_values"][self.job]
        array[2] = self.lable["marital_values"][self.marital] 
        array[3] = self.lable["education_values"][self.education] 
        array[4] = self.lable["default_values"][self.default] 
        array[5] = self.balance
        array[6] = self.lable["housing_values"][self.housing]
        array[7] = self.lable["loan_values"][self.loan]
        array[8] = self.lable["contact_values"][self.contact]
        array[9] = self.day
        array[10] = self.lable["month_values"][self.month]
        array[11] = self.duration
        array[12] = self.campaign
        array[13] = self.pdays
        array[14] =self.previous

        subscription = self.model.predict([array])[0]

        #print(self.lable["y_values_rev"][str(subscription)])
        return self.lable["y_values_rev"][str(subscription)]
    
if __name__ == "__main__":
    age                    = 73
    job                    = "retired"
    marital                = "married"
    education              = "secondary" 
    default                = "no"
    balance                = 2850
    housing                = "no"
    loan                   = "no"
    contact                = "cellular"
    day                    = 17
    month                  = "nov"
    duration               = 300
    campaign               = 1 
    pdays                  = 40
    previous               = 8

    obj = Term_deposit(age,job,marital,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous)
    print("\n\nwill client subscribe the term deposit ?",obj.get_prediction(),"\n\n")