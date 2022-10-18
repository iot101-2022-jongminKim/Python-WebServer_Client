import requests
URL = "http://127.0.0.1:8000"
d = {'sid':2019146008,'name':'Jongmin'}
r = requests.post(url=URL, data=d)
print(r.status_code)
print(r.text)