import requests
import time

r = requests.post('http://httpbin.org/post', json={"key": "value"})
#print(r.status_code)

timestamp = int(time.time())
r.json()
{
    "time": timestamp,
    "acao": "entrada",
    "portao": "principal"
}
