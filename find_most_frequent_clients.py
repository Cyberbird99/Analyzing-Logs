'''
I intend to employ regular expressions (regex) to extract essential data 
from log files in order to identify clients engaged in specific activities. 
My objective is to determine the individual or 
IP address that has accessed a particular website most frequently. 
I want to see the clients who visit the site most often. 
To achieve this, I'll utilize the 're' library, which is a Python module for working with regex
'''
import re

# Request the file to be analyzed.
log_file = input("What file will you anlayze? ")

# Open the file and load its contents into memory.
with open(log_file, "r") as f:
    access_logs = f.readlines()

# Establish a regular expression pattern and an empty dictionary.
client_search_pattern = r'(^\S+\.[\S+\.]+\S+)\s'
clients = {}

# Find the match and store in the dictionary
for line in access_logs:
    # Look for the pattern, and if detected, proceed.
    m = re.search(client_search_pattern, line)
    if m:
        client = m.group()
        # Store the access frequency in the dictionary.
        if client in clients.keys():
            clients[client] += 1
        else:
            clients[client] = 1

# Sort by most frequenlty accessed
for w in sorted(clients, key=clients.get, reverse=False):
    print(w, clients[w])
