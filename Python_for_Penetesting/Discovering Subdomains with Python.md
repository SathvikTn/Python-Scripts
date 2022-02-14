# Discovering Subdomains with Python

Valid Subdomains are found and printed. Here u can use threads to faster the process.

#### subdomain.py
---------------------------------------------------------------------
```python
import requests 
import sys 

sub_list = open("subdomains.txt").read() 
subs = sub_list.splitlines()

for sub in subs:
    check_url = f"http://{sub}.{sys.argv[1]}"     # f-strings are for string fromatting. here {sub} is replaced with sub in every loop.

    try:
        requests.get(check_url)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",check_url)

```

Execute -> python subdomain.py google.com

Output -> Prints valid subdomains

List of subdomains -> (999 to be exact)

### Suggested readings:

[subdomains.txt](https://github.com/SathvikTn/Python-Scripts/blob/master/subdomains.txt)
