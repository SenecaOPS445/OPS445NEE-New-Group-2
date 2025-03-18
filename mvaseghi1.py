import os

# Make the list of IPs
    ip_list = make_ip_list(start_ip, end_ip)
    
    # Check if list was created successfully
    if len(ip_list) > 0:
        print(f"Created list with {len(ip_list)} addresses.")
        print("Starting ping test for all IPs in the range...")
        
        # Ping each IP in the list
        for ip in ip_list:
            ping_ip(ip)
    else:
        print("No IPs to ping due to invalid input")


# Function to ping an IP
def ping_ip(ip):
    if os.name == "nt":  # Windows
        command = "ping -n 2 " + ip
    else:  # Linux/Unix
        command = "ping -c 2 " + ip
    result = os.system(command)
    if result == 0:
        print(f"{ip} is UP")
    else:
        print(f"{ip} is DOWN")