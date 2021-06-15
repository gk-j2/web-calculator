import requests
import sys

input = sys.argv[1]
params = input.split(',')
num1 = float(params[0])
num2 = float(params[1])
operation = params[2]

url = 'http://18.118.113.198/calc/my_api/v1/'

headers = {
    'content-type': 'application/json'
}

payload = {
    "a":num1,
    "b":num2,
    "operation":operation
    }

reply = requests.post(url=url, headers=headers, json=payload)

text = reply.text
if text.startswith("Error"):
    answer = text
else:
    answer = text.split(':')[1]
    answer = answer[0:len(answer)-2]

print(f"Answer: {answer}")