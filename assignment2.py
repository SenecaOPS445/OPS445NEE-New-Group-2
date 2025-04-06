#!/usr/bin/env python3
import sys
import os
import ipaddress

def ping_ip(ip):
    '''Pings an IP address and prints if it's up or down'''
    if os.name == "nt":  # Windows
        command = "ping -n 2 " + ip
    else:  # Linux/Unix
        command = "ping -c 2 " + ip
    result = os.system(command)
    if result == 0:
        print(f"{ip} is UP")
        return True
    else:
        print(f"{ip} is DOWN")
        return False

def check_ip_range(start_ip, end_ip):
    '''Creates IP list from range using provided iprangetolist function and pings each address'''
    try:
        # Make the list of IPs using groupmate's function
        ip_list = iprangetolist(start_ip, end_ip)
        
        # Check if list was created successfully
        if len(ip_list) > 0:
            print(f"Created list with {len(ip_list)} addresses.")
            print("Starting ping test for all IPs in the range...")
            Total_ip_up = 0
            Total_ip_down = 0

            # Ping each IP in the list
            for ip in ip_list:
                if ping_ip(ip):
                    Total_ip_up +=1
                else:
                    Total_ip_down +=1
            print (f"{Total_ip_up} IPs are up")
            print (f"{Total_ip_down} IPs are down")
        else:
            print("No IPs to ping due to empty range")
            
    except ValueError as e:
        print(f"Error: Invalid IP address format - {e}")
    except Exception as e:
        print(f"Error: {e}")

def check_ip_subnet(subnet):
    '''Creates IP list from range using provided iprangetolist function and pings each address'''
    try:
        # Make the list of IPs using groupmate's function
        ip_list = ipsubnettolist(subnet)
        
        # Check if list was created successfully
        if len(ip_list) > 0:
            print(f"Created list with {len(ip_list)} addresses.")
            print("Starting ping test for all IPs in the range...")
            Total_ip_up = 0
            Total_ip_down = 0
            
            # Ping each IP in the list
            for ip in ip_list: 
                if ping_ip(ip):
                    Total_ip_up +=1
                else:
                    Total_ip_down +=1
            print (f"{Total_ip_up} IPs are up")
            print (f"{Total_ip_down} IPs are down")
        else:
            print("No IPs to ping due to empty range")
            
    except ValueError as e:
        print(f"Error: Invalid IP address format - {e}")
    except Exception as e:
        print(f"Error: {e}")
 
 
def iprangetolist(startip, endip):
    '''Takes 2 ip addresses and returns a list of addresses in that range'''
    iplist = [startip] # initializes the list with the first ip address
    ip = startip
    while ip != endip: #iterrates through ip addresses until it reaches the end address
        ip = str(ipaddress.IPv4Address(ip) + 1)
        iplist.append(ip)
    return iplist

def ipsubnettolist(subnet):
    '''Takes an ip with a subnet and converts it to a list of host addesses in the subnet'''
    iplist = list(ipaddress.IPv4Network(subnet, strict=False).hosts()) # Creates a list of host addresses
    iplist = list(map(str, iplist)) # Converts the items in the list to strings
    return iplist

def validate_ip(ip_to_check):
    try:
        ipaddress.IPv4Address(ip_to_check)
        return True
    
    except ipaddress.AddressValueError as e:
        print (f"Error: Invalid IP address - {e})")
        return False
    except ValueError as e:
        print (f"Error: {e}")
        return False

def validate_ip_in_range(range_start, range_end):
    try:    
        start_ip = ipaddress.IPv4Address(range_start)
        end_ip = ipaddress.IPv4Address(range_end)
            
        if start_ip > end_ip:
                start_ip = end_ip
                end_ip = start_ip
                print("Start IP is > End IP")
                print("Swaping Start IP and End IP")
                return True
        return True
                
    except ipaddress.AddressValueError as e:
        print (f"Error: Invalid IP address - {e})")
        return False
    except ValueError as e:
        print (f"Error: {e}")
        return False
    
def validate_ip_in_subnet(ip_to_check, subnet):
    try:
        ip = ipaddress.IPv4Address(ip_to_check)
        
        network = ipaddress.IPv4Network(subnet, strict=False)
        if ip in network:
                print(f"IP {ip_to_check} is within subnet {subnet}")
                return True
        print(f"Error: IP {ip_to_check} is not in subnet {subnet}")
        return False
    
    except ipaddress.AddressValueError as e:
        print (f"Error: Invalid IP address - {e})")
        return False
    except ValueError as e:
        print (f"Error: {e}")
        return False
    

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if validate_ip(sys.argv[1]):
            ping_ip(sys.argv[1]) 
        elif validate_ip_in_subnet(sys.argv[1].split('/')[0],sys.argv[1]):
            check_ip_subnet(sys.argv[1]) 
    
    elif len(sys.argv) == 3:
        if sys.argv[1] == sys.argv[2]:
            print ('The Frist Argument is the same as the Second Argument')
            print ('Skiping Srcond Argument')
            if validate_ip(sys.argv[1]):
                ping_ip(sys.argv[1])  
        elif validate_ip_in_range(sys.argv[1], sys.argv[2]):
            check_ip_range(sys.argv[1], sys.argv[2])
    
    else:
        print("Useage: messege..")