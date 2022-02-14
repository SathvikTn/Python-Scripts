import sys
import nmap
#to use nmap module in python, u need to pip install python-nmap
#check the installed version of nmap by "pip show python-nmap"
#Name: python-nmap
#Version: 0.6.1
#Summary: This is a python class to use nmap and access scan results from python3
#Home-page: http://xael.org/pages/python-nmap-en.html

#afer installing, open nmap folder and open nmap.py and go to def scan(): section
#in that, go to #launch scan on line 224 in nmap.py
#change args from
#args = [self._nmap_path, '-oX', '-'] + h_args + ['-p', ports] * (ports is not None) + f_args
#to
#args = [self._nmap_path, '-T4', '-A', '-oX', '-'] + h_args + ['-p', ports]*(ports is not None) + f_args
#also u need to have nmap installed on your system.

if len(sys.argv) < 2 :
    print("Usage : python " + sys.argv[0] + " <ip address> ") #prints how to execute the code
    sys.exit(1)

target = str(sys.argv[1])

scan_v = nmap.PortScanner()   #scan variable
print("Scanning", target, "for all available ports...... \n")

#ports = [21,22,80,139,443,8080]  #for specific ports use this ...
#print("Scanning", target, "for"  + ports \n")
#for port in ports:
#   portscan = scan_v.scan(target,port)

port_scan = scan_v.scan(target) #type of port_scan is 'dict'
#print(port_scan, "\n")  #to print the whole output

print("Hostname :", port_scan["scan"][target]["hostnames"][0]["name"])  #to print hostname
addrs = port_scan["scan"][target]["addresses"]
for ver in addrs:
        print(ver, ":", addrs[ver])  #ver is ipv4 or ipv6 and addrs is ip addresses.
print("State :", port_scan["scan"][target]["status"]["state"], "\n")

openports = port_scan["scan"][target]["tcp"]    #to print ports that are open and info on them
for port, j in openports.items():
    #print(port_scan["scan"][target]["tcp"])
    print("Port :", port)
    for i in j:
        if str(j[i]) == "":
            continue
        else:
            print(i, ":", j[i])
    print("\n")

os = port_scan["scan"][target]["osmatch"][0]
for i in os:
    if str(i) == "osclass":    #to print osclass dictionary elements
        j = os["osclass"]
        for k in j:
            for l in k:
                print(l, ":", k[l])
            print("\n")
    else:
        print(i, ":", os[i])    #other elements in osclass dict are printed
