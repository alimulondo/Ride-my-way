"""
  Author: Ali Mulondo
  Date: 18/06/2018
  About: This file contains all my apiv1 data processing..
 
"""

  ### 1 A list of offers dictionaries
offers_list = [{ "offid":101, "ownerid":501, "offstatus":1, "offdate":"18/06/2018 10:30Am", 
"offcontent":"AM leaving at 11:00Am and hope to reach at 12:00Pm", "offfrom":"Kyenjojo", "offto":"mbalala"},
{ "offid":102, "ownerid":501, "offstatus":0, "offdate":"18/06/2018 10:30Am", 
"offcontent":"AM leaving at 11:00Am and hope to reach at 12:00Pm", "offfrom":"Kyenjojo", "offto":"mbalala"},
{ "offid":103, "ownerid":501, "offstatus":1, "offdate":"18/06/2018 10:30Am", 
"offcontent":"AM last here", "offfrom":"Busitema", "offto":"Kampala"}
]

  ### 2 A list of request dictionaries
req_list = [
  {"reqid":1000, "reqowner":2000, "offid":101,
    "reqdate":"18/06/2018 10:50Am", "reqstatus":0,
    "msg":"can i join you at 11:00am from  masaka? " 

  }

  ]

  ### 3 A list of riders/drivers details

  ### 4 A list of passengers details

def  sendData():
	 return offers_list

def addData(data):
 	offers_list.append(data)
 	return "ok"

# request sub-helper functions

def reqdataSend():
	return req_list
def reqdataAdd(data):
 	req_list.append(data)
 	return "ok"

def retData():
	return offers_list

def retreqData():
	return req_list	


