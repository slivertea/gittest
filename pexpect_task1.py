#!/usr/bin/python3.6
import pexpect
import re
username = 'ignw'
password = 'ignw'
device_ip = '10.0.0.5'

connection = pexpect.spawn(f'ssh {username}@{device_ip}')

#print(connection)
#print(type(connection))

# - print the login steps
connection.expect('Password:')
connection.sendline(password)
connection.expect('ignw-csr#')
#print(connection.before)
#print(connection.after)
# - hostname grabber
#   the blow sets hostname based on the config
command = "show run | in hostname"
connection.sendline(command)
connection.expect('ignw-csr#')
hostname = re.sub(".*hostname\s", "", str(connection.before))
hostname = hostname[:2]
print("printing by config parse:")
print(hostname)
# the REM'd block blow sets hostname based on the prompt
connection.sendline(command)
connection.sendline("\n")
hostname = connection.after[:1]
print(hostname)
#
command = "show run int g1"
connection.sendline(command)
connection.expect('ignw-csr#')
interface_output = connection.before
print(type(interface_output))
print(connection.after)
# - parse the interface output, and split each sendline
split_output = interface_output.decode().split('\r\n')
#print(split_output)
# - now parse that further cleanly to call each line into a variable during a loop
# - draconian method of matching with split
print("Matches all by draconian methods, ie split:")
for line in split_output:
    #print(line)
    if line.startswith("interface"):
        intname = line[10:]
        print(intname)
    elif line.startswith(" description"):
        intdesc = line[13:]
        print(intdesc)
    elif line.startswith(" ip address"):
        intip = line[12:]
        print(intip)
    elif line.startswith(" vrf"):
        intvrf = line[13:]
        print(intvrf)



print("Match by regex")
for line in split_output:
    intname = re.findall('interface.*', line)
    print(intname)
