import os

def ping_ip(ip):
    '''Pings an IP address and prints if it's up or down'''
    if os.name == "nt":  # Windows
        command = "ping -n 2 " + ip
    else:  # Linux/Unix
        command = "ping -c 2 " + ip
    result = os.system(command)
    if result == 0:
        print(f"{ip} is UP")
    else:
        print(f"{ip} is DOWN")

def check_ip_range(start_ip, end_ip, iprangetolist):
    '''Creates IP list from range using provided iprangetolist function and pings each address'''
    try:
        # Make the list of IPs using groupmate's function
        ip_list = iprangetolist(start_ip, end_ip)
        
        # Check if list was created successfully
        if len(ip_list) > 0:
            print(f"Created list with {len(ip_list)} addresses.")
            print("Starting ping test for all IPs in the range...")
            
            # Ping each IP in the list
            for ip in ip_list:
                ping_ip(ip)
        else:
            print("No IPs to ping due to empty range")
            
    except ValueError as e:
        print(f"Error: Invalid IP address format - {e}")
    except Exception as e:
        print(f"Error: {e}")