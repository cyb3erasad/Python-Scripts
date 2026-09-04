# Nmap Recon Scanner (Python)

A simple CLI tool that automates Nmap scans, filters results to show open ports/services, flags common high-risk ports, and saves timestamped reports — built as hands-on practice for SOC analyst fundamentals.

## Features
- Choose between Basic, Version Detection (-sV), or Aggressive (-A) scans
- Filters raw Nmap output to just open ports/services
- Flags commonly risky open ports (FTP, Telnet, RDP, HTTP) with short analyst-style notes
- Saves each scan as a timestamped .txt report

## Tech
- Python 3 (subprocess module)
- Nmap
- Tested in Kali Linux (VirtualBox)

## Usage
```bash
python3 scan.py
```
You'll be prompted for a target and a scan type. Results print to screen and save to a report file in the same directory.

## Example output

--- Open Ports/Services ---
22/tcp open ssh
80/tcp open http

--- Summary ---
Total open ports found: 2
⚠ Port 80 open — HTTP (unencrypted) — check if HTTPS (443) is also available


## Disclaimer
Only scan systems you own or have explicit permission to test (e.g. scanme.nmap.org).

## Next steps
- Multi-target scanning from a list
- Compare scans over time to detect changes
- Export as CSV/JSON for easier log analysis