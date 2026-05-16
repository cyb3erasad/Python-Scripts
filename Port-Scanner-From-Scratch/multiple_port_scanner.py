import socket

target = "scanme.nmap.org"  # A legal host made for practicing scans
ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]

print(f"\nPort scanning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # Don't wait more than 1 second per port

    result = s.connect_ex((target, port))

    if result == 0:
        print(f" [open] Port {port}")
    else:
        print(f" [Closed] Port {port}")

    s.close()        
