#!/usr/bin/env python3

import sys
import ipaddress
 
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
    iplist = list(ipaddress.ip_network(subnet).hosts()) # Creates a list of host addresses
    iplist = list(map(str, iplist)) # Converts the items in the list to strings
    return iplist
    

if __name__ == '__main__':
    print(iprangetolist('192.168.1.10','192.168.1.20'))
    print(ipsubnettolist('192.168.1.0/29'))