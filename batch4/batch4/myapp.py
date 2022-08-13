import requests
import json

url = "http://127.0.0.1:8080/att/student_api/"
'''
j1 = {"id":2}

json_data = json.dumps(j1)
r = requests.get(url= url, data=json_data)

print (r)
print (r.json())
'''

def postdata():
	data = { 'stuid' : 40, "stuname": "hjk", "stumail" : "klj@xyz.com"  }
	json_data = json.dumps(data)
	r = requests.post(url=url, data=json_data)
	data = r.json()
	print (data)

def putdata():
	#data = { 'stuid' : 30, "stuname": "JKLK", "stumail" : "klj@xyz.com"  }
	data = { 'stuid' : 30, "stuname": "JK" }
	json_data = json.dumps(data)
	r = requests.put(url=url, data=json_data)
	data = r.json()
	print (data)

def deletedata():
	data = {'stuid':30}
	json_data = json.dumps(data)
	r = requests.delete(url=url, data=json_data)
	data = r.json()
	print (data)


postdata()