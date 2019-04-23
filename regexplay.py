#!/usr/bin/python3.6
import re

ifip = "ip address 192.168.0.1 255.255.255.0"
#ipmask = re.compile(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b')
ipcompile = re.compile(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\s')
ipparsed = ipcompile.search(ifip)

print(ipcompile)
print(f'"before: " + {ifip}')
print(f'"after : " + {ipparsed.group()}')



ifip = "ip address 192.168.0.1 255.255.255.0"
print("##################################")

ipparsed = ipcompile.findall(ifip)
for each_ip in ipparsed:
    print("eachIP:")
    print(each_ip)
