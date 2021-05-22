#!/usr/bin/env python3

import subprocess as sub
import optparse
import re

def arguments():
	parser = optparse.OptionParser()

	parser.add_option('-i', '--interface', dest='interface', help="for Interface")
	parser.add_option('-m', '--mac', dest='mac', help="for MAC")

	(options, arguments) = parser.parse_args()

	if not options.interface:
		parser.error('* Make sure you specify an interface!')
	elif not options.mac:
		parser.error('* Make sure you specify a new mac address!')
	return options

def mac_changer(interface, mac):
	ifconfig = sub.check_output(['ifconfig', options.interface]).decode('utf-8')

	pattern = "\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" #pattern for MAC addresses	
	old_mac_address = re.search(pattern, ifconfig) #search specific pattern on ifconfig result 	
	if old_mac_address:
		print("Old MAC =>",old_mac_address.group(0))
	print('\n> Changing MAC address (' + interface + ') to ' + mac)


	if re.match(pattern, options.mac) != re.match(pattern, mac):
		#steps to change MAC
		sub.call(["ifconfig", interface, "down"])
		sub.call(["ifconfig", interface, "hw", "ether", mac])
		sub.call(["ifconfig", interface, "up"])
	else: 
		print('Invalid MAC address!')
def ifconfig(interface):
	ifconfig = sub.check_output(['ifconfig', options.interface]).decode('utf-8')

	pattern = "\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" #pattern for MAC addresses
	mac_address = re.search(pattern, ifconfig) #search specific pattern on ifconfig result 

	if mac_address:
       		print("\nNew MAC =>", mac_address.group(0)) 
	else:
       		print('No MAC address on this interface!') #if interface does not have a MAC

	if mac_address.group(0) == options.mac:
		print('(+) Successfully changed!')
	else:
		print('(-) Unsuccessful attempt!')

options = arguments()
mac_changer(options.interface, options.mac)
ifconfig(options.interface)




