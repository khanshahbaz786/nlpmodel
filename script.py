#!/usr/bin/env python
import sys, json
import subprocess
# Load the data that PHP sent us
#output = subprocess.check_output(["php", welcome.php, input1])
try:
    data = sys.argv[1]
	
except:
    print "Sachin"
    sys.exit(1)

# Generate some data to send to PHP
#result = "Python"
print data
# Send it to stdout (to PHP)
data='Sachin'+data
print json.dumps(data)