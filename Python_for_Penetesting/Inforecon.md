# Inforecon
## Grabbing Banners, Hostname and IP Lookup 

First we're going to code a banner grapper. Then we're going to look up host names and then we're going to do IP look up. All in Python.

Now first for banner grabbing, we'll be using the Requests module and we'll make a GET request to the server and then print that response.

When you make a request, the Response Headers reveal important information about the server.

How it works is that we provide a command line argument containing the address of the site that we want to grab the banner for it.

Code goes as below :-

#### [Inforecon.py](https://github.com/SathvikTn/Python/blob/master/inforecon.py) 
------------------------------------------------------------------------------------------------------------------------------------------
```bash
pip install requests for requests module
```

```python
import sys
import requests
import socket
import json

#Usage
if len(sys.argv) < 2 :
print(Usage : python  + sys.argv[0] +  <url> ) #prints how to execute the code
sys.exit(1)

#Step 1
#banner grabbing is to gather information about something. here we will get info on sites.

req = requests.get(https:// + sys.argv[1])
print(\n + str(req.headers))

#Step 2
#to get host names, we use socket module's function get host by name

ip = socket.gethostbyname(sys.argv[1])
print(\nIP address of https:// + sys.argv[1] +  is -  + ip + \n)

#Step 3
#IP look up - to get location of this IP in latitude and longitude
#For that, we are gonna make a request to an api that provides this kind of service
#that api is ipinfo.io and we provide the ip address and format as json

req1 = requests.get(https://ipinfo.io/+ip+/json)
res = json.loads(req1.text)

print(Hostname : +res[hostname])
print(location : +res[loc])
print(City : +res[city])
print(Region : +res[region])
print(Country : +res[country])
print(Org : +res[org])
print(Postal : +res[postal])
print(Timezone : +res[timezone])
```
------------------------------------------------------------------------------------------------------------------------------------------

### Suggested readings:

requests module: https://requests.readthedocs.io/en/master/

sys module: https://docs.python.org/3/library/sys.html

json module: https://docs.python.org/3/library/json.html

socket module: https://docs.python.org/3/library/socket.html

