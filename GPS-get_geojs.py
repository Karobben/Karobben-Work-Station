#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
origin version:
https://www.freecodecamp.org/forum/t/make-a-script-read-gps-geolocation/241607
'''


import requests
import time

# Step 1) Find the public IP of the user. This is easier said that done, look into the library Netifaces if you're
# interested in getting the public IP locally.
# The GeoIP API I'm going to use here is 'https://geojs.io/' but any service offering similar JSON data will work.

#print(my_ip)
# Prints The IP string, ex: 198.975.33.4

# Step 2) Look up the GeoIP information from a database for the user's ip
f = open("log",'a')
def run():
    while True:
        ip_request = requests.get('https://get.geojs.io/v1/ip.json')
        my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data = geo_request.json()
        #print(geo_data)
        Result = time.asctime().split(' ')[-2]+'\t'+geo_data["latitude"]+"\t"+geo_data["longitude"]+"\n"
        f.write(Result)
        time.sleep(0.6)

try:
    run()
except:
    pass
