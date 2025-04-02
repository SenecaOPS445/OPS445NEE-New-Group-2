#!/usr/bin/env python3

import ipaddress
import os

def validate_ip_in_range(ip_to_check, range_start=None, range_end=None, subnet=None):
    try:
        ip = ipaddress.IPv4Address(ip_to_check)
        
        if subnet:
            network = ipaddress.IPv4Network(subnet, strict=False)
            if ip in network:
                return f"IP {ip_to_check} is within subnet {subnet}"
            return f"Error: IP {ip_to_check} is not in subnet {subnet}"
        
        if range_start and range_end:
            start_ip = ipaddress.IPv4Address(range_start)
            end_ip = ipaddress.IPv4Address(range_end)
            
            if start_ip > end_ip:
                return "Error: Start IP must be <= End IP"
                
            if start_ip <= ip <= end_ip:
                return f"IP {ip_to_check} is within range {range_start}-{range_end}"
            return f"Error: IP {ip_to_check} is not in range {range_start}-{range_end}"
        
        return "Error: Must provide either subnet or both range_start and range_end"
            
    except ipaddress.AddressValueError as e:
        return f"Error: Invalid IP address - {e}"
    except ValueError as e:
        return f"Error: {e}"

def ping_ip(ip):
    """Pings an IP address and prints status"""
    if os.name == "nt":
        command = f"ping -n 2 {ip}"
    else:
        command = f"ping -c 2 {ip}"
    result = os.system(command)
    print(f"{ip} is {'UP' if result == 0 else 'DOWN'}")

def check_ip_range(start_ip, end_ip, iprangetolist):
    """Checks all IPs in range using ping"""
    try:
        ip_list = iprangetolist(start_ip, end_ip)
        if not ip_list:
            print("No IPs to ping (empty range)")
            return
            
        print(f"Pinging {len(ip_list)} IPs...")
        for ip in ip_list:
            ping_ip(ip)
            
    except ValueError as e:
        print(f"Error: {e}")

def iprangetolist(startip, endip):
    """Generates list of IPs between two addresses"""
    iplist = [startip]
    ip = startip
    while ip != endip:
        ip = str(ipaddress.IPv4Address(ip) + 1)
        iplist.append(ip)
    return iplist

def ipsubnettolist(subnet):
    """Generates list of host IPs in a subnet"""
    return [str(host) for host in ipaddress.ip_network(subnet).hosts()]

if __name__ == '__main__':
    print(validate_ip_in_range("192.168.1.15", range_start="192.168.1.10", range_end="192.168.1.20"))
    print(validate_ip_in_range("192.168.1.25", subnet="192.168.1.0/29"))
    
    print(iprangetolist("192.168.1.10", "192.168.1.15"))
    print(ipsubnettolist("192.168.1.0/29"))

    check_ip_range("192.168.1.1", "192.168.1.3", iprangetolist)