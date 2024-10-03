import requests
import json

url = "https://vh4xhmjk3lw2ibz5k6sa4i6fym0ltkqv.lambda-url.us-east-1.on.aws/"

payload = {
    "ipaddress": '54.225.154.233:5000' # Public IPv4 address which you can find on the EC2 instance home page. Add port number on which your server is running (5000). Do NOT include "http://" in the IP address!
}


print("Running the autograder. This might take several seconds...")

r = requests.post(url, data=json.dumps(payload), headers = {"Content-Type": "application/json"})

print(r.status_code, r.reason)
print(r.text)
