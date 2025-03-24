#!/usr/bin/env python3

import ipaddress

# User database with requested users
users = {
    "Sultan": {
        "password": "secure123",
        "allowed_ips": ["192.168.1.0/24", "10.0.0.0/8"]
    },
    "Jakob": {
        "password": "jakobpass",
        "allowed_ips": ["172.16.0.0/12"]
    },
    "Mohammad": {
        "password": "mohammad456",
        "allowed_ips": ["203.0.113.0/24"]
    },
    "Olivia": {
        "password": "olivia789",
        "allowed_ips": ["198.51.100.0/24"]
    }
}

def login(username, password, ip_address):
    if username in users:
        user = users[username]
        if user["password"] == password:
            for subnet in user["allowed_ips"]:
                if ipaddress.ip_address(ip_address) in ipaddress.ip_network(subnet):
                    return f"Login successful for {username} from {ip_address}"
            return f"Access denied for {username} from {ip_address}. IP not in allowed subnets."
        else:
            return "Incorrect password."
    else:
        return "User not found."

def add_user(username, password, allowed_ips):
    if username in users:
        return "User already exists."
    else:
        users[username] = {
            "password": password,
            "allowed_ips": allowed_ips
        }
        return f"User {username} added successfully."

# Test cases
print(login("Sultan", "secure123", "192.168.1.100"))  
print(login("Jakob", "jakobpass", "172.16.0.1"))       
print(login("Mohammad", "mohammad456", "203.0.113.5"))     
print(login("Olivia", "olivia789", "198.51.100.10"))    
print(login("Olivia", "wrongpass", "198.51.100.10"))   
print(login("Unknown", "password", "192.168.1.1"))     

# Test adding a new user
print(add_user("NewUser", "newpass", ["192.168.3.0/24"]))  
print(login("NewUser", "newpass", "192.168.3.100"))