# Winter 2025 Assignment 2

This is a Python script developed as a group project to ping IP addresses, supporting single IPs, IP ranges, and subnets. It validates input, generates lists of IPs to scan, pings them, and provides a summary of which machines are up or down.

**Project Overview
**The script takes command-line arguments to specify an IP address, a range of IPs, or a subnet. It then:

**Validates the input for correctness.
**Generates a list of IPs to ping (for ranges or subnets).
Pings each IP using the system's ping command.
Outputs the results in a human-readable format, including a summary of up and down IPs.

**Features**
Single IP Ping: Pings a single IP address (e.g., 192.168.1.1).
IP Range Ping: Pings a range of IPs (e.g., 192.168.1.1 to 192.168.1.3), swapping if the start IP is greater than the end IP.
Subnet Ping: Pings all host IPs in a subnet (e.g., 192.168.1.0/30).
Validation: Ensures IPs are valid (0.0.0.0 to 255.255.255.255) and subnets have a valid network address.
Output: Displays real-time ping results and a summary of up/down IPs.
