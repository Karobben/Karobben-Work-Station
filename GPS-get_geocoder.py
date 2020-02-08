#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
origin version:
https://blog.csdn.net/longwei92/article/details/88750723
'''

import geocoder

g = geocoder.ip('me')
print(g.current_result,g.latlng)



'''
g = geocoder.ip('199.7.157.0')
g.city

Search GPS information
http://www.gpsspg.com/maps.htm
'''
