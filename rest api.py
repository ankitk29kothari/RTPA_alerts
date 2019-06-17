import requests
import json


url=('https://tt-gateway5.orange-business.com/serviceApi/qa/user/addNewUser?key=SHARED_KEY')
headers = {'Content-type': 'application/json'}


data= {
"emailId":"pooja.garg@orange.com",
"password":"smile@123"
}




r = requests.post(url, data=json.dumps(data), headers=headers)
print( r.status_code)
print (r.json())