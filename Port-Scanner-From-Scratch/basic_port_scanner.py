import socket

# socket.AF_INET  = IPv4 address family
# socket.SOCK_STREAM = TCP connection (reliable, handshake-based)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = s.connect_ex(("google.com", 80))

# connect_ex returns 0 if connection succeeded, error code if failed
print(result)
s.close()