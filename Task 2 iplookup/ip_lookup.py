
import requests
import csv
from datetime import datetime

def create_ips_file():
    ips = [
        "121.127.64.72",
        "162.43.143.200",
        "77.214.254.242",
        "57.166.175.50",
        "62.111.224.144",
        "136.131.33.245",
        "52.245.54.118",
        "60.118.27.168",
        "86.57.64.142",
        "252.78.152.40"
    ]
    with open('ips.txt', 'w') as f:
        for ip in ips:
            f.write(ip + '\n')
    print(" ips.txt created successfully!")

def main():
    create_ips_file()
    
    with open('ips.txt', 'r') as f:
        ips = [line.strip() for line in f if line.strip()]
    
    results = []
    log_entries = []
    
    print(" Starting IP lookups...\n")
    
    for ip in ips:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        city = "Unknown"
        status = None
        error = None
        
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/geo", timeout=10)
            status = response.status_code
            
            if response.status_code == 200:
                data = response.json()
                city = data.get('city', 'Unknown')
                print(f" {ip} → {city}")
            else:
                error = f"HTTP {status}"
                print(f" {ip} → HTTP Error {status}")
                
        except Exception as e:
            error = str(e)[:100]
            print(f" {ip} → Failed")
        
        results.append([ip, city])
        
        log_line = f"{timestamp} | IP: {ip} | Status: {status} | City: {city}"
        if error:
            log_line += f" | Error: {error}"
        log_entries.append(log_line)
    
    # Write CSV
    with open('ip_locations.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ip', 'city'])
        writer.writerows(results)
    
    # Write Log
    with open('ip_lookup.log', 'w') as f:
        f.write("\n".join(log_entries))
    
    print("\n Task 2 Completed Successfully!")
    print("Files created: ips.txt, ip_locations.csv, ip_lookup.log")

if __name__ == "__main__":
    main()
