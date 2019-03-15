from pymongo import MongoClient
import sys
import json
import re

# True for verbose output of Mongo instance and database listing
DEBUG = False

if not len(sys.argv) == 3:
    print "Usage: %s ipFile resultsFile" % (sys.argv[0])
    exit()
inFile = sys.argv[1]
outFile = sys.argv[2]

# Generate list of IP addresses from ipFile
f = open(inFile)
lines = f.read()
ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}',lines)
ips = set(ips)
f.close()

print "Preparing to scan %d IP addresses" % (len(ips))

for ip in ips:

    # Try and connect to MongoDB. Requires no authentication.
    c = MongoClient(ip, 27017, serverSelectionTimeoutMS=1000,connectTimeoutMS=1000,socketTimeoutMS=1000,waitQueueTimeoutMS=1000)
    try:
        # This operation will fail if DB authentication is required
        c.server_info()

        if DEBUG:
            print (json.dumps(c.server_info(), indent=4, sort_keys=True))
            print (json.dumps(c.database_names(), indent=4, sort_keys=True))

        f = open(outFile, 'a')
        f.write(str(ip) + '\n')
        f.close()

        print "SUCCESS -- Connected to open MongoDB at IP %s" % (str(ip))

    except Exception,e:
        if DEBUG:
            print e

        pass

    c.close()
