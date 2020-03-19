import osmnx as ox
import urllib
import threading
# from optparse import OptionParser
# from bs4 import BeautifulSoup
# import sys
import re
from urllib.parse import urlparse
import queue
import hashlib
import math
import os
from geopy.distance import geodesic
import urllib.request
import json

class StreetScanner(object):
    '''
    input: two nodes(the start of the street and the end of the street), length
    return: the images
    '''
    def __init__(self, c1, c2, length, StreetName):
        self.c1 = c1
        self.c2 = c2
        self.length = length
        self.StreetName = StreetName

    def truecoordinate(self,url):
        conn = urllib.request.urlopen(url)
        a = conn.read() #下载meta
        a = a.decode('utf-8')
        j = json.loads(a)
        if 'location' not in j:
            return None
        lat = j['location']['lat']
        lon = j['location']['lng']
        return (str(lat),str(lon))

    def download(self, url, name):
        # path = "C:\\Users\\Administrator\\Desktop\\pictures"
        #url = "http://pic2.sc.chinaz.com/files/pic/pic9/201309/apic520.jpg"
        #url = "https://maps.googleapis.com/maps/api/streetview?size=600x300&location=46.414382,10.013988&heading=151.78&pitch=-0.76&key="#你的KEY"

        conn = urllib.request.urlopen(url)
        f = open(name, 'wb')
        f.write(conn.read())
        f.close()
        print('Pic Saved!') 

    def get_url(self):
        numbers = self.length // 10
        numbers = int(numbers)
        if self.c2[1] == self.c1[1]:
            heading = str(180)
        else:
            heading = str(math.degrees(math.atan((self.c2[0] - self.c1[0]) / (self.c2[1] - self.c1[1]))) + 90)
        
        for i in range(numbers):
            lon = str(self.c1[0] + i * ((self.c2[0] - self.c1[0]) / numbers))
            lat = str(self.c1[1] + i * ((self.c2[1] - self.c1[1]) / numbers))
            
            metadataurl =  "https://maps.googleapis.com/maps/api/streetview/metadata?size=640x640&location=" + lat + "," + lon + "&heading=" + heading + "&key="
            coordinate = self.truecoordinate(metadataurl)
            if not coordinate:
                continue
            lat, lon = coordinate
            # name = "C:\\Users\\Yang\\Desktop\\master project\\pictures\\" + self.StreetName + "\\" + lat + "_" + lon + "_" + heading + "_FrontView.JPG"
            # url = "https://maps.googleapis.com/maps/api/streetview?size=640x640&location=" + lat + "," + lon + "&heading=" + heading + "&key="
            #print zu
            # if os.path.exists(name):
            #     print('have same picture!')
            #     continue
            #print url
            # self.download(url, name)

if __name__ == "__main__":
    pass
