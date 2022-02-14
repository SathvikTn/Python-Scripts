# The Socket Module for Network Communication - A TCP Server-Client

In this, you're going to learn about TCP communication and how to build a TCP server and client.

We have two python programs client.py and server.py. Server is going to listen or wait for the messages and client is going to send the messages. 
Understanding how client and server works -- 

#### client.py
---------------------------------------------------------------------
```python
import socket

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
sock_.connect(host)

msg = sock_.recv(1024)     # number of bytes you want to receive
sock_.close()
print(msg.decode("ascii"))
```

---------------------------------------------------------------------

#### server.py
---------------------------------------------------------------------
```python
import socket

host = socket.gethostname()   # in string
port = 9337   # random port number

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Address Family - Internet
# Sock_stream for TCP and DGRAM for UDP

sock_.bind((host, port))
sock_.listen(1)
# 1 is the number of backlog i.e, number of the unaccepted connections before this server refusing new connections

print("Server Started .....!!!!!")

conn, addr = sock_.accept()

print("connection established with", str(addr))
msg = "Thank you for connecting "+str(addr)
conn.send(msg.encode("ascii"))
conn.close()
```