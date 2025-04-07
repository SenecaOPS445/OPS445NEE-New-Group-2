#!/usr/bin/env python3
import os
import ipaddress
import argparse

'''This program takes an IP address or network address as an argument and pings the address or all addresses in the given subnet
If the user specifies an IP address as the second argument, it is interpreted as a range and all the addresses are pinged'''
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
            # counters to check the total number of successful pings and failed pings
            total_ip_up = 0
            total_ip_down = 0

            # Ping each IP in the list
            for ip in ip_list:
                if ping_ip(ip):
                    # if the ping is successful, the counter bellow goes up by one
                    total_ip_up +=1
                else:
                    # if the ping failed, the other counter goes up
                    total_ip_down +=1
                    # these results are printed
            print (f"{total_ip_up} IPs are up")
            print (f"{total_ip_down} IPs are down")
        else:
            print("No IPs to ping due to empty range")
        
        '''If there is a problem converting the input to an IP address the code bellow will print an error message'''

    except ValueError as e:
        print(f"Error: Invalid IP address format - {e}")
        ''' if there is any other problem with the code, the line bellow will print an error message'''
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
            total_ip_up = 0
            total_ip_down = 0
            
            # Ping each IP in the list
            for ip in ip_list: 
                if ping_ip(ip):
                    # if the ping is successful, the total_ip_up 
                    total_ip_up +=1
                else:
                    total_ip_down +=1
            print (f"{total_ip_up} IPs are up")
            print (f"{total_ip_down} IPs are down")
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
    while ip < endip: #iterrates through ip addresses until it reaches the end address
        ip = str(ipaddress.IPv4Address(ip) + 1)
        iplist.append(ip)
    return iplist

def ipsubnettolist(subnet):
    '''Takes an ip with a subnet and converts it to a list of host addesses in the subnet'''
    iplist = list(ipaddress.IPv4Network(subnet, strict=True).hosts()) # Creates a list of host addresses
    iplist = list(map(str, iplist)) # Converts the items in the list to strings
    return iplist

'''Function to check if IP addresses are valid
Takes one mandatory argument: an IP address and another mandatory argument: a second IP address'''
def validate_ip(first_ip, last_ip = None):
    try:
        # first, the function checks if a second IP address was passed in
        if last_ip:
            # if yes, it checks that the second IP address is greater than the first IP address preventing errors later in the program
            if ipaddress.IPv4Address(last_ip) > ipaddress.IPv4Address(first_ip):
                # if the condition is true, the function returns true
                return True
            # if the IP addresses are past in reverse order, the function returns false
            return False
        # if there is no second argument, the function just checks the validity of the IP address passed to it
        elif ipaddress.IPv4Address(first_ip):
            # if the IP address is valid, the function returns true
            return True
        
    # if the IP address is not valid, this will be caught by the except statement and the function will print the error and return false
    except ipaddress.AddressValueError as e:
        print (f"Error: Invalid IP address - {e})")
        return False
    except ValueError as e:
        print (f"Error: {e}")
        return False
        


if __name__ == '__main__':
    
    # create a argparse object 
    parser = argparse.ArgumentParser(description="Ping IPs or check IP ranges/subnets.")
    
    # first IP or subnet is an optional argument; add the "ip_or_subnet" argument
    # I decided to make this argument optional as well, because I want the program to print the help message if no input is provided  
    parser.add_argument("ip_or_subnet", nargs="?", help="An IP address or subnet to ping.")
    
    # second IP is a optional argument (hence, nargs='?'; add the "end_ip" argument
    parser.add_argument("end_ip", nargs="?", help="End IP address for a range (optional).")
   
    # retrieve the arguments supplied by the user
    args = parser.parse_args()
    
    # if there is only one IP address specified:
    if args.ip_or_subnet and not args.end_ip:
        
       
        # if the first argument contains a "/" then that means we want to ping all the IPs in the subnet
        if '/' in args.ip_or_subnet:
            
            # ping all IPs in the subnet 
            check_ip_subnet(args.ip_or_subnet)
            
         # check if the IP address specified is valid before doing anything else
        elif validate_ip(args.ip_or_subnet):
            
            # if the IP is valid, execute a ping command to the IP 
            ping_ip(args.ip_or_subnet)
        

    # if two arguments specified 
    elif args.ip_or_subnet and args.end_ip:

        if args.ip_or_subnet == args.end_ip:
            print('The First Argument is the same as the Second Argument')
            print('Skipping Second Argument')
            if validate_ip(args.ip_or_subnet):
                ping_ip(args.ip_or_subnet)
        
        #check if end_ip is greater than starting ip...
        elif(validate_ip(args.ip_or_subnet, args.end_ip)):
            
            # if end_ip is greater than starting ip, then check all those ips...
            check_ip_range(args.ip_or_subnet, args.end_ip)
            
        
        else: # if the end_ip is less than the starting ip, then switch end_ip with starting ip, and check all ips...
             print("Start IP is > End IP")
             print("Swaping Start IP and End IP")
             check_ip_range(args.end_ip, args.ip_or_subnet)
        
    
    else:
        # if the user doesn't supply any input, a help message with an explanation of each argument is printed
        parser.print_help()