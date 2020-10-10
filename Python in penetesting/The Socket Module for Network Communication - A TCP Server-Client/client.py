import socket

sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
sock_.connect(host)

msg = sock_.recv(1024)     # number of bytes you want to receive
sock_.close()
print(msg.decode("ascii"))

