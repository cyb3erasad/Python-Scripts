import subprocess
from datetime import datetime

def run_scan(target, scan_type):
    if scan_type == "1":
        command = ["nmap", target]
    elif scan_type == "2":
        command = ["nmap", target]
    elif scan_type == "3":
        command = ["nmap", target]
    else:
        print("Invalid choice, running on default scan.")
        command = ["nmap", target]
    
    result = subprocess.run(command, capture_output=True, text=True)
    open_ports = [line for line in result.stdout.splitlines() if "open" in line]

    print("\n--- Open Ports/Servcies ---")
    for line in open_ports:
        print(line)

    filename = f"scan_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(f"Scan of {target}\n")
        f.write(f"Time: {datetime.now()}\n\n")
        f.write("\n".join(open_ports))

        print(f"\nResults saved to {filename}")
        return filename, open_ports

def summarize(open_ports):
    print("\n--- Summary ---")
    print(f"Total open ports found: {len(open_ports)}")

    risky_ports = {"21": "FTP (often insecure)",
                   "23": "Telnet (umcrypted, high risk)",
                   "3389": "RDP (common attack target)",
                   "80": "HTTP (unencrypted) - check if HTTPS (443) is also available"}

    for port_num, warning in risky_ports.items():
        for line in open_ports:
            if line.startswith(port_num + "/"):
               print(f"Port {port_num} open - {warning}")

def main():
    target = input("Enter target to scan: ")

    print("\nChoose scan type:")
    print("1. Basic Scan")
    print("2. Version Detection (-sV)")
    print("3. Aggressive Scan (-A)")
    scan_type = input("Enter choice (1/2/3): ")

    filename, open_ports = run_scan(target, scan_type)
    summarize(open_ports)

if __name__ == "__main__":
    main()

