# Finding Hidden Wireless Networks with Python

Hidden SSID is a feature to hide your netwrok, and what happens is that it doesn't add SSID to beacon frames. Beacon Frame is a frame containg all information about the netwrok. But it is not the efficient way to hide your network since SSID is added to probe requests and responses.

Lets see how to find hidden SSID ->

Requirements ->
Network card that supports monitor mode

What we will be doing is ->
We will disconnect the client connected to a hidden network and then the client tries to reconnect back.

#### hiddenwifi.py
---------------------------------------------------------------------
```python
from scapy.all import *
import os

iface = "wlan0"    # default wifi card... change it accordingly if using other.

def h_packet(packet):
    if packet.haslayer(Dot11ProbeReq) or packet.haslayer(Dot11ProbeResp) or packet.haslayer(Dot11AssoReq):
        print "SSID identified " + packet.info

os.system("iwconfig " + iface + "mode monitor")

print "Sniffing traffic on interface " + iface
sniff(iface=iface, prn=h_packet)
```
---------------------------------------------------------------------