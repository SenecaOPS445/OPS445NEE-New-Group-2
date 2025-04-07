# Winter 2025 Assignment 2

Our program pings an IP address, range of IP addresses or a subnet specified by a network address and CIDR "/" prefix.

The program gathers user input using argparse.
There are two parameters ip_or_subnet and end_ip. Both are optional and a help message is printed if none are given.
The script differentiates between an IP address and network ID with a series of a few if statements and the "in" keyword used to search for a "/" in the ip_or_subnet argument to check if the user wants to ping a subnet.
The ipaddress Python library and the .IPv4Address method are used extensivelly throughout the script to simplify IP address parsing.
The program uses functions for specific tasks including validating IP addresses, creating lists of addresses and pinging addresses.
The OS library is used to execute the ping commands.
The main method for error handing in the program are try and accept statements, most of which handle cases where user input can't be converted to an IPv4 address by the ipaddress.Pv4Address method because it is invalid. 
Pinging a range of IP addresses or a subnet is handled by creating a list of every possible IP address in the range or subnet with the help of the ipaddress library.

The output is presented in plain text using print statements and fstrings.

Jakob: For me the most challenging part was dealing with the error checking and trying to account for all the possible errors the user could encounter. Another challenging part was migrating away from sys.argv and learning to use argparse. It takes some getting used to but once you get the hang of it. It can be faster than sys.argv especially for implementing quick documentation for your arguments as we did in the program.  

Questions:

How will your program gather required input?
How will your program accomplish its requirements?
How will output be presented?
What arguments or options will be included?
What aspects of development do you think will present the most challenge?
When do you estimate you will complete each part of the task? Provide a rough timeline for planning, coding, testing, and documenting your assignment.
This meeting will be a dialogue, since there might be some changes or suggestions that come up during our initial meeting.

Once you have gotten approval for your script, you will get access to your repository for development. Include the description, overview and summary of the above questions inside your repository's README.md file.