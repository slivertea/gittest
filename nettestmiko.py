#!/usr/bin/python3.6
import re
import netmiko
from netmiko import ConnectHandler
cisco_cloud_router = {'device_type': 'cisco_ios',
'ip': '10.0.0.5',
'username': 'ignw',
'password': 'ignw'}
connection = ConnectHandler(**cisco_cloud_router)
#print(connection)
#print(type(connection))

hostname = connection.find_prompt()
#print(hostname[:-1])
ifip = connection.send_command('show run int g2 | i address')
if re.search(r'((\d{1,3}\.){3}(\d{1,3}))', ifip):
    #print(ifip)
    ipaddr = re.search(r'((\d{1,3}\.){3}(\d{1,3}))',ifip)
    print(ipaddr.group())
else:
    print("No IP Found")

print(ifip)
