# mscan
mscan is a simple scanner to find open MongoDB instances. Our intention is to create a very easy way to scan IP ranges for MongoDB databases running default configurations, which implement near-zero security, and no authentication required to access the databases. 

# Installation
The only library dependency mscan has is on PyMongo. See [installation instructions here](http://api.mongodb.com/python/current/installation.html), or simply run:

`$ python -m pip install pymongo`

Pull down this repository:

`git clone https://github.com/sidechainconsulting/mscan.git`

and run mscan:

`python mscan.py infile outfile`

# Setup
mscan requires an input file of IP addresses to scan, one per line. 

For example, *inputfile.txt*:
```
192.168.1.1
192.168.1.2
192.168.1.3
```

A convenient way to create output of IP address ranges is to use __nmap__:

`$ nmap -sL -n 192.168.1.0/30 | grep 'Nmap scan report for' | cut -f 5 -d ' '`

There is also a __Debug__ mode you can put mscan in by altering the value on line 7. Turning on __Debug__ will output additional information about the MongoDB instance. Both the instance info and a list of databases running in the instance are captured.

# Usage Example
Create a file of IP addresses, called *ipfile*:
```
162.243.52.49
192.168.1.1
162.243.52.50
13.59.2.52
192.241.229.61
52.199.158.48
160.16.238.21
```

Copy the file into the same directory as *mscan.py*. 

Run mscan:
`python mscan.py ipfile outfile`

Output to the screen should look something like:
```
Preparing to scan 7 IP addresses
SUCCESS -- Connected to open MongoDB at IP 192.241.229.61
SUCCESS -- Connected to open MongoDB at IP 160.16.238.21
SUCCESS -- Connected to open MongoDB at IP 13.59.2.52
SUCCESS -- Connected to open MongoDB at IP 52.199.158.48
```

This indicates that of all the IP addresses scanned, those four were insecure MongoDB databases. Those IP's were written to the file *outfile* in our example.

# About Sidechain
Sidechain is a data security consulting and service delivery firm. We help our clients create and deploy security solutions protecting their most valuable data. We work with both individuals as well as organizations across the globe. To speak with us about securing your data, email us at *hello@sidechainconsulting.com*.

