import subprocess
from datetime import datetime

def run_scan(target, scan_type):
    if scan_type == "1":
        command = ["nmap", target]
    elif scan_type == "2":
        command = ["nmap", "-sV", target]
    elif scan_type == "3":
        command = ["nmap", "-A", target]
    else:
        print("Invalid Choice, running default scan.")
        command = ["nmap", target]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    open_ports = [line for line in result.stdout.splitlines() if "open" in line]

    print("\n--- Open Ports/Services ---")
    for line in open_ports:
        print(line)

    
    filename = f"scan_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(f"Scan of {target}\n")
        f.write(f"TIme {datetime.now()}\n\n")
        f.write("\n".join(open_ports))

    print(f"\nResults saved to {filename}")

def main():
    target = input("Enter target to scan: ")

    print("\nChoose scan type:")
    print("1. Basic Scan")
    print("2. Version Detection (-sV)")
    print("3. Aggressive Scan (-A)")
    scan_type = input("Enter choice (1/2/3): ")

    run_scan(target, scan_type)


if __name__ == "__main__":
    main()
