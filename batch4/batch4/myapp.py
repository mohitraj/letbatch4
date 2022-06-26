import requests
import json

url = "http://127.0.0.1:8080/att/student_api/"

j1 = {"id":2}

json_data = json.dumps(j1)
r = requests.get(url= url, data=json_data)

print (r)
print (r.json())