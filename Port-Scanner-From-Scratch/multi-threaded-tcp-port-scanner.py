import socket
import threading
from datetime import datetime

Target = "scanme.nmap.org"
Port_Range = range(1, 1025)
Timeout = (1)
Threads = 100

open_ports = []
lock = threading.Lock()  # Prevent race conditions when writing results

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(Timeout)
        result= s.connect_ex((Target, port))

        if result == 0:
            with lock:   # Thread-safe append
                open_ports.append(port) 
        s.close()        

    except socket.error:
        pass            

def run_scanner():
    print(f"\n{'='*45}")
    print(f" Target : {Target}")
    print(f" Ports : {Port_Range.start} - {Port_Range.stop - 1}")
    print(f" Started : {datetime.now().strftime('%H:%M:%S')}")
    print(f"\n{'='*45}")

    threads = []

    for port in Port_Range:
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()
        
        # Run in batches to avoid overwhelming the system
        if len(threads) >= Threads:
            for t in threads:
                t.join()
            threads = []
    
    # Wait for remaining threads
    for t in threads:
        t.join()

    print(f"Scan complete at {datetime.now().strftime('%H:%M:%S')}")

    if open_ports:
        for port in sorted(open_ports):
            print(f"[OPEN] Ports {port}")
    else:
        print("No open port found")                        

run_scanner()