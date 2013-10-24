#AUTHOR: Sh1n0b1
#Yes, it's sloppy

import requests
import sys
import re

if(len(sys.argv) <= 1):
	print "\tpython proxy.py [ip:port]"
	sys.exit()

arg = sys.argv[1];

target = 'https://ctf.fluxfingers.net/ref/MyHl7CtvFtdqnfX';
#check = 'http://checkip.dyndns.com/';

proxy_port = {'http' : "http://" + arg.rstrip()};

print "Proxy\t\t\t\t\tActual IP\t\t\tResponse";

def req(url, proxies):
	try:
		r = requests.get(url, proxies=proxies, verify=False, timeout=20)
		IP = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", r.text);
		print IP,
		print r.text;
	except requests.exceptions.Timeout:
		print "Timeout";
	except requests.exceptions.ConnectionError:
		print "Error";
	except requests.packages.urllib3.exceptions.ProxyError:
		print "Error";

print proxy_port,
req(target, proxy_port);

