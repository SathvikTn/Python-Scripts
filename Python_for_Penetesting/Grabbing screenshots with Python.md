# Grabbing Screenshots with Python

Here we are going to use python to capture screenshots and additionally, we are going to upload it to an ftp server.

For that you need wxPython, so 
```bash
pip install wxpython
```
and import it as wx. We also need to import os and ftplib.

To access files on ftp server, open file explorer, ad type ftp://serverIP then enter username and password.

Follow the code below, which saves the screenshot locally in the folder where the code exists and also it uploads to ftp server.

#### Code
---------------------------------------------------------------------
```python
import wx #pip install wxPython
import os
import ftplib
import time

print(Taking Screenshot......)
for i in range(5, 0, -1):
print(i)
time.sleep(i) #sleeping for 5 sec

w = wx.App() # instance of wx
screen = wx.ScreenDC() # used to paint on screen that is to capture the screen
size = screen.GetSize() # size of the screenshot that is size of device's screen
bmap = wx.Bitmap(size[0], size[1]) # create a bitmap with width and height of source screen
# next we need is a memory device which enables us to draw graphics onto bitmap
mem = wx.MemoryDC(bmap) # to write onto bitmap
mem.Blit(0, 0, size[0], size[1], screen, 0, 0) # copy from sourceDC to this DC
# here first two 0's are postion for x and y of destination device, then size[0] and [1] are width
# and height, screen is the source from what we copy, and finally x and y of source device context.

del mem # delete mem since we dont need it anymore
# to save bitmap as bmg
name = input(Enter the name for the screenshot without any spaces : )
# file is saved in the folder where this program is saved.
bmap.SaveFile(name+.png, wx.BITMAP_TYPE_PNG)
# default -> bmap.SaveFile(screeshot.png, wx.BITMAP_TYPE_PNG)

# to use ftp server, u need to install iis manager from 'turn windows features on or off'
# in control panel
'''

server_ip = input(Enter the ip address of ftp server : )
user = input(Enter username : )
password = input(Enter password : )
# to upload to ftp server, we need a session
sess = ftplib.FTP(server_ip, user, password) #to create a connection, call it with args - host,user,password,acct,and timeout
# ftp server we use is metasploitable 2
file = open(screenshot.png, rb) #rb - read binary
sess.storbinary(STOR /tmp/+name+.png, file)
# to view the screenshot, u can open the /tmp folder in server.

file.close()
sess.quit()

'''
```
---------------------------------------------------------------------

### Suggested readings:

wxPython documentation: https://wxpython.org/

pyscreenshot package: https://pypi.org/project/pyscreenshot/
