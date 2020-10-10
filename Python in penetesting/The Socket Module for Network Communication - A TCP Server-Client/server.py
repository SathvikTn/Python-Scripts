
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
