import os
import re
import socket
import sys
import netmiko
from getpass import getpass

username = input("Username: ")
password = getpass() 


def to_doc_w(file_name, varable):
	f=open(file_name, 'w')
	f.write(varable)
	f.close()	
	
def to_doc_a(file_name, varable):
	f=open(file_name, 'a')
	f.write(varable)
	f.close()


def pull_run(username,password,net_connect,ip):
	hostname = net_connect.find_prompt()[:-1]
	running_config = hostname + " running_config.txt"
	to_doc_w(running_config, net_connect.send_command_expect('show run'))


def get_ip (input):
	return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))

		
def get_ips (file_name):
	for line in open(file_name, 'r').readlines():
		line = get_ip(line)
		for ip in line: 
			ips.append(ip)
ips = []
get_ips("IPs.txt")

for ip in ips:
	net_connect = netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)
	pull_run(username,password,net_connect,ip)

	
