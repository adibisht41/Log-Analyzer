# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:49:50 2018

@author: Aditya
"""

import time
import json
import re
StartTime = time.time()
def convert():
    Keys=['IP Address',
     'User Agent',
     'X Request From',
     'Request Type',
     'API',
     'User Login',
     'User Name',
     'EnterpriseId',
     'EnterpriseName',
     'Auth Status',
     'Status Code',
     'Response Time',
     'Request Body']
    diction={}
    log_entries=0
    with open('log.txt', 'r') as f:
        for entry in f:
            text = entry.rstrip('\n')
            regex2 = re.compile("(IP-Address|User-Agent|Status-Code|Request-Type|API|User-Name|EnterpriseId|EnterpriseName|Auth-Status|X-Request-From|User-Login|Response-Time|Request-Body)")
            iter = regex2.finditer(text) #returns an iterator over all non-overlapping matches for the regular expression pattern in the string.
            indices = [m.start(0) for m in iter]
            Values = []
            for x in range(len(indices)-1):
                CurrentValue = text[indices[x]+len(Keys[(x)%13])+1:indices[x+1]-3]
                Values.append(CurrentValue)
            
            CurrentValue = text[indices[12]+len(Keys[12])]
            CurrentValue = CurrentValue[1:]
            temp = CurrentValue
            CurrentValue=""
            for i in temp:
                if (i=='\n'):
                    break
                CurrentValue = CurrentValue+i 
            Values.append(CurrentValue)
            
            diction[log_entries]={}
            count=0
            for i in Values:
                diction[log_entries][Keys[count]] = i
                count=count+1
            log_entries=log_entries+1
    
    ############ SAVING FILE TO JSON#############
    JsonString = json.dumps(diction)
    f = open("dict.json","w")
    f.write(JsonString)
    f.close()
    #############################################

convert()
print("--- %s seconds ---" % (time.time() - StartTime))