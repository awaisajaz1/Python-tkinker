import urllib.request as urllib2
import ssl
import pandas as pd 
import json
from pandas.io.json import json_normalize
import sqlalchemy
#!pip install mysql-connector==2.1.4
from datetime import datetime
from tkinter import *
#import plotly.graph_objs as go
import numpy as np 
from dateutil.parser import parse as ps
from sqlalchemy import select
from sqlalchemy.sql import and_




def run():
#    now = datetime.datetime.now()
#    dt= now.strftime("%Y-%m-%d")
# Reading data from online sensor HTTP Protocal
    start_date = txtentry.get()
    end_date = txtentry2.get() 
#    url = 'https://*****************8/api/v1/venues/tmelab-01/metrics/impressions.json?start_date=2018-06-20&end_date=2018-06-24'
#    username = 'BfIOqE5Kf11b1Z0pNKY0tQsGBpKEA7Oc3V29zvnazukSBbAoB2TAsGTqlrbaahWH'
#    password = 'x'
#    p = urllib2.HTTPPasswordMgrWithDefaultRealm()
#    p.add_password(None, url, username, password)
#    handler = urllib2.HTTPBasicAuthHandler(p)
#    opener = urllib2.build_opener(handler)
#    urllib2.install_opener(opener)
#    page = urllib2.urlopen(url).read()
#    context = ssl._create_unverified_context()
    #response = urllib2.Request('https://*****************8/api/v1/venues/tmelab-01/metrics/impressions.json?start_date='+dt+'&end_date='+dt)
    #response = urllib2.Request('https://*****************8/api/v1/venues/tmelab-01/metrics/impressions.json?start_date='+start_date+'&end_date='+end_date+'&granularity=hourly')
    response = urllib2.Request('https://*****************8/api/v1/venues/tmelab-01/locations/last_known.json?seconds_ago=1000000')
    
    #response = urllib2.Request('https://*****************8/api/v1/venues/tmelab-01/metrics/impressions.json?start_date=2018-06-04&end_date=2018-07-04')
    ssl._create_default_https_context = ssl._create_unverified_context
    response3 = urllib2.urlopen(response)
    sensor = response3.read()
#converting to json format 
    data = json.loads(sensor)
    try:
        while data['status'] == 'processing':
            output.delete(0.0,END)
            output.insert(END,'Request Generated please wait Data is on the way')
            #print(data['status'] == 'processing')
            if data['status'] == 'processing':
                print("Request Generated please wait Data is on the way")
            #response = urllib2.Request('https://*****************8/api/v1/venues/tmelab-01/metrics/impressions.json?start_date=2018-06-04&end_date=2018-07-04')
            response = urllib2.Request('https://*****************8/api/v1/venues/tmelab-01/locations/last_known.json?seconds_ago=300')
            ssl._create_default_https_context = ssl._create_unverified_context
            response3 = urllib2.urlopen(response)
            sensor = response3.read()
            data = json.loads(sensor)
#            if data['status'] == 'processing':
#                output.delete(0.0,END)
#                output.insert(END,"Data is Processing please try again")
#            elif len(data[0]) > 0:
#                output.delete(0.0,END)
#                output.insert(END,"Data has been succesfully fetched")
    except Exception:
        data = json.loads(sensor)
    if data:
        print("Data has been fetched")
        global data1
        data1 = data
        output.delete(0.0,END)
        output.insert(END,'Data Fetched Succesfully')
    return data
    
time = ['2018-07-09T04:00:00-07:00','2018-07-09T05:00:00-07:00']

#def start():



    
def parse():
   
    #tslog2 = pd.DataFrame()
    for i in data1:
        sensor_DF_date = i['timestamp']
        sensor_DF_date= ps(sensor_DF_date)
        sensor_DF = pd.DataFrame([i])
        se = pd.Series(sensor_DF_date) 
        sensor_DF['datetime'] = se.values
        df1 = sensor_DF.ix[:, ['floor_number', 'located_inside' ,'mac' ,'x','y','datetime' ]]
        df1.to_sql(con=database_connection, name='rukuswireless_mac' , if_exists = 'append')
        with open('H:\Python Workspace\py\my_csv.csv', 'a') as f:
            sensor_DF.to_csv(f, header=False)
            output3.delete(0.0,END)
            output3.insert(END,'DATA PARSED SUCCESFULLY AND INSERTED TO DATABASE')
        output4.delete(0.0,END)
        output4.insert(END,count)
#    
  
if __name__ == '__main__':
################################################# DATABASE CONNECTION########################################
    database_username = 'ETL_USER'
    database_password = 'HC1ETL1'
    database_ip       = 'xxx.xxx.xxx.xx'
    database_name     = 'DEMO_R'
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                               database_ip, database_name))
    
################################################# URL CONNECTION############################################
    url = 'https://*****************8/api/v1/venues/tmelab-01/locations/last_known.json?seconds_ago=60'
    username = 'BfIOqE5Kf11b1Z0pNKY0tQsGBpKEA7Oc3V29zvnazukSBbAoB2TAsGTqlrbaahWH'
    password = 'x'
    ssl._create_default_https_context = ssl._create_unverified_context
    p = urllib2.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(p)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    #page = urllib2.urlopen(url).read()
################################################# Tkinter Main###############################################
    window = Tk()
    window.title("Hive Tools")
################################################### GUI AREA#################################################
    Label (window, text = "HIVEWORX WEB URL REQUEST FORM" , bg = 'grey',fg='white', font = 'non 10 bold').grid(row=0, column =0, sticky=W)
##Button
    Button(window, text ='Fetch Data', width = 10 , command = run).grid(row=3,column = 0,sticky = W)
    #Button(window, text ='set Data', width = 10 , command = start).grid(row=7,column = 0,sticky = W)

##text entry of Date to fetch
    Label (window, text = "STARTDATE" , bg = 'grey',fg='white', font = 'non 10 bold').grid(row=1, column =0, sticky=W)
    txtentry = Entry(window, width =20 , bg = 'white')
    txtentry.grid(row=2,column = 0,sticky = W)
    Label (window, text = "ENDDATE" , bg = 'grey',fg='white', font = 'non 10 bold').grid(row=1, column =1, sticky=W)
    txtentry2 = Entry(window, width =20 , bg = 'white')
    txtentry2.grid(row=2,column = 1,sticky = W)
##Out put
    output = Text(window, width = 50 , height = 1 , wrap = WORD , background = 'white')
    output.grid(row=3,column = 1,sticky = W)

    window.mainloop()    
################################################### 2nd GUI AREA#################################################
    window2 = Tk()
    window2.title("Data Base")
    Label (window2, text = "HIVEWORX Data Parsing Section" , bg = 'grey',fg='white', font = 'non 10 bold').grid(row=0, column =0, sticky=W)
##Button
    Button(window2, text ='Parse Data', width = 10 , command = parse).grid(row=1,column = 0,sticky = W)
    #Button(window, text ='set Data', width = 10 , command = start).grid(row=7,column = 0,sticky = W)
##Out put
    output3 = Text(window2, width = 55 , height = 1 , wrap = WORD , background = 'white')
    output3.grid(row=3,column = 0,sticky = W)
    
    Label (window2, text = "Number of Dictionaries Parsed:" , bg = 'grey',fg='white', font = 'non 10 bold').grid(row=4, column =0, sticky=W)
    output4 = Text(window2, width = 15 , height = 1 , wrap = WORD , background = 'white')
    output4.grid(row=4,column = 0,sticky = E)

    window2.mainloop() 




            
            
            





