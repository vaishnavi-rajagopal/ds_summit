import requests
url='https://lf8q0kx152.execute-api.us-east-2.amazonaws.com/default/computeFitnessScore'
x=requests.post(url,json={"qconfig":"4 6 0 3 1 7 5 2","userID":174098,"githubLink":"https://github.com/vaishnavi-rajagopal/ds_summit/blob/master/Queens.py"})
print(x.text)
