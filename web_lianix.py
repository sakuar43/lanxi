import socket

host_name = socket.gethostname()
print("Host name %s" % host_name)
print("IP Addresses: %s" % socket.gethostbyname(host_name))
