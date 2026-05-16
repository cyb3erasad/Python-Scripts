import socket

def grab_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect_ex((ip, port))

        # Send a generic HTTP request — many services respond to this
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024).decode("utf-8", errors="ignore").strip()
        s.close()

        return banner
    
    except:
        return None
    
target = "scanme.nmap.org"
ports = [22, 80, 443]

for port in ports:
    banner = grab_banner(target, port)

    if banner:
        print(f"\n[Port {port}]  Banner:\n{banner[:200]}")
    else:
        print(f"\n[Port {port}] No banner recieved")    

