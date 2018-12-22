#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
██╗███╗   ██╗███████╗███╗   ███╗ █████╗  ██████╗ ██╗ ██████╗
██║████╗  ██║██╔════╝████╗ ████║██╔══██╗██╔════╝ ██║██╔════╝
██║██╔██╗ ██║█████╗  ██╔████╔██║███████║██║  ███╗██║██║
██║██║╚██╗██║██╔══╝  ██║╚██╔╝██║██╔══██║██║   ██║██║██║
██║██║ ╚████║██║     ██║ ╚═╝ ██║██║  ██║╚██████╔╝██║╚██████╗
╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝
        Version: 0.2 Codename: "Oblivious Bison"

What:
	Takes a list of IPs as input and outputs the associated CIDRs based on WHOIS information.

Dependencies:
	ipwhois & docopt (both can be pip installed)

Usage:
	infmagic.py [-h] [-c OUTPUT1] [-s OUTPUT2] -i INPUT


Options:
  -h --help           show this
  -c --csv OUTPUT1   save output as CSV
  -s --sql OUTPUT2    save output as SQLite (TODO!)
  -i INPUT            list of IPs to use

"""
#TODO: REMOVE THIS it's a temporary fix for ipwhois
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
from ipwhois import IPWhois

from pprint import pprint
from docopt import docopt
import csv, signal, os


def signal_handler(signal, frame):
		print_error ('System Interupt requested, attempting to exit cleanly!')
		os._exit(0)

signal.signal(signal.SIGINT, signal_handler)

class bcolors:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERL = '\033[4m'
	ENDC = '\033[0m'
	backBlack = '\033[40m'
	backRed = '\033[41m'
	backGreen = '\033[42m'
	backYellow = '\033[43m'
	backBlue = '\033[44m'
	backMagenta = '\033[45m'
	backCyan = '\033[46m'
	backWhite = '\033[47m'

def print_status(message):
	print(bcolors.GREEN + bcolors.BOLD + "[*] " + bcolors.ENDC + str(message))

def print_info(message):
	print(bcolors.BLUE + bcolors.BOLD + "[-] " + bcolors.ENDC + str(message))

def print_info_spaces(message):
	print(bcolors.BLUE + bcolors.BOLD + "  [-] " + bcolors.ENDC + str(message))

def print_warning(message):
	print(bcolors.YELLOW + bcolors.BOLD + "[!] " + bcolors.ENDC + str(message))

def print_error(message):
	print(bcolors.RED + bcolors.BOLD + "[!] " + bcolors.ENDC + bcolors.RED + str(message) + bcolors.ENDC)

def ip2CIDR(ipN):
	for ip in ipN:
		try:
			w = IPWhois(ip)
		except:
			pass
#TODO: I need to move to RDAP at some point!
		# for i in w.lookup_rdap():
		# 	for x in i['cidr'].split(','):
		# 		entry_ip = ip  #Original IP address
		# 		entry_asn = w.lookup()['asn'] #ASN Value
		# 		entry_cidr = x.strip() #CIDR Value
		# 		entry_desc = i['description'].replace('\n', ' ').replace('\r', ' ')
		#
		# 		print_info ("New entry: %s, %s, %s, %s" % (entry_ip, entry_asn, entry_cidr, entry_desc))
		for i in w.lookup_whois()['nets']:
			for x in i['cidr'].split(','):
				entry_ip = ip  #Original IP address
				try:
					entry_asn = w.lookup_whois()['asn'] #ASN Value
				except:
					#pass
					entry_asn = "N/A"
				try:
					entry_cidr = x.strip() #CIDR Value
				except:
					entry_cidr = "N/A"
				try:
					entry_desc = i['description'].replace('\n', ' ').replace('\r', ' ')
				except:
					entry_desc = "N/A"
				print_info ("New entry: %s, %s, %s, %s" % (entry_ip, entry_asn, entry_cidr, entry_desc))


				if arguments['--csv']:
					#print "CSV: %s" % arguments['--csv']
					with open('./%s' % arguments['--csv'], 'a') as f:
						writer = csv.writer(f)
						writer.writerow([entry_ip, entry_asn, entry_cidr, entry_desc])
					pass




def main():
	with open(arguments['-i']) as f:
		client_ips = [_f for _f in [line.strip('\n').strip() for line in f] if _f]

	if arguments['--csv']:
		with open('./%s' % arguments['--csv'], 'w') as f:
			writer = csv.writer(f)
			writer.writerow(["Original IP","ASN Value","CIDR Value","Description"])
			print_status ("Saving %s..." % (bcolors.GREEN + bcolors.BOLD + arguments['--csv'] + bcolors.ENDC))

	ip2CIDR(client_ips)

	print_status ("All done! KTHXBYE...")


if __name__ == '__main__':
	arguments = docopt(__doc__, version='InfMagic 0.1')
	#print(arguments)
	main()
