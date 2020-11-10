import json
import re
import subprocess

dict1 = {}
#dict2 = {}

text = subprocess.run(['sudo', 'dmidecode', '-t', '17'], stdout=subprocess.PIPE).stdout.decode('utf-8')

with open(text) as fh:
  for line in fh:

    #command = (r'^Handle\s(.+?),\sDMI\stype\s(\d+?),\s(\d+?)\sbytes$')
    #dict1
    k, v = [line.strip() for line in fh.split(':', 1)]
    k[dict1] = v.strip()
    print(k)