# I'm writing a python code to find a 401 error 
# from a log file.
# My sample log file is in data folder.
# 401 the client request has not completed because it lacks
# valid authentication credentials

# Request the file to be analyzed.
log_file = input("Type a file name to analyze. ")

# Access the file now
f = open(log_file, 'r')

# Read the file line by line
while True:
    line = f.readline()
    if not line:
        break
    # Verify the presence of "401" in the content.
    if "401" in line:
        print(line.strip())

# Close file
f.close()