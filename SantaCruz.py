import osmnx as ox
import os
from StreetScanner import StreetScanner
from tqdm import tqdm
from coordinatedistance import CoordinateDistance
from geopy.distance import geodesic
import mpu
import math
import json
import urllib.request
places = ['Santa Cruz downtown, California, USA',
          {'city':'Santa Cruz','county':'Santa Cruz', 'state':'California'}]
G = ox.graph_from_place(places,retain_all = True, network_type='drive')
os.chdir("C:/Users/Yang/Desktop/master project/pictures")
B = set()

A = list(G.edges())
print(A)
Anew = list(G.edges())
print(len(A))
for i in range(len(A)):
    if (A[i] not in B) and ((A[i][1],A[i][0]) not in B):
        B.add(A[i])    
print(len(B))
B = list(B)

C = []
calculate = CoordinateDistance()
D = []
for i,j in B:
    lon1 = G.node[i]['x'] #lon
    lat1 = G.node[i]['y'] #lat
    lon2 = G.node[j]['x'] #lon
    lat2 = G.node[j]['y'] #lat
    distance = geodesic((lat1, lon1),(lat2, lon2)).meters

    length = G[i][j][0]['length']
    if length > 0.95 * distance and length < 1.05 * distance and length > 20:
        C.append((i,j))

print(len(C))


acc= 0


def truecoordinate(url,lat,lon):

    conn = urllib.request.urlopen(url)
    a = conn.read() #下载meta
    a = a.decode('utf-8')
    j = json.loads(a)
    if 'location' not in j:
        return (lat,lon)
    lat = j['location']['lat']
    lon = j['location']['lng']
    return (lat,lon)


# for i,j in tqdm(C):   #i,j is the node id

#     if  'name' not in G[i][j][0]:
#         continue

#     print(G[i][j][0])

#     if type(G[i][j][0]['name']) is list: #if list then just take first street name
#         G[i][j][0]['name'] = G[i][j][0]['name'][0]

#     os.makedirs(G[i][j][0]['name'],exist_ok=True)

#     StreetName =G[i][j][0]['name']
#     length = G[i][j][0]['length']
#     lon1 = G.node[i]['x'] #lon
#     lat1 = G.node[i]['y'] #lat
#     lon2 = G.node[j]['x'] #lon
#     lat2 = G.node[j]['y'] #lat
#     if lat1 == lat2:
#         headding = 180
#     else:
#         heading = math.degrees(math.atan((lon2 - lon1) / (lat2 - lat1))) + 90
#     url = "https://maps.googleapis.com/maps/api/streetview/metadata?size=640x640&location=" + str(lat1) + "," + str(lon1) + "&heading=" + str(heading) + "&key=AIzaSyCC_bzL68dKT0ha3pqvB4Q_1Hk75nU5TvQ"
#     url2 = "https://maps.googleapis.com/maps/api/streetview/metadata?size=640x640&location=" + str(lat2) + "," + str(lon2) + "&heading=" + str(heading) + "&key=AIzaSyCC_bzL68dKT0ha3pqvB4Q_1Hk75nU5TvQ"
#     lat1,lon1 = truecoordinate(url,lat1,lon1)
#     lat2,lon2 = truecoordinate(url2,lat2,lon2)
#     if lat1==lat2:
#         headding2 = 180
#     else:
#         heading2 = math.degrees(math.atan((lon2 - lon1) / (lat2 - lat1))) + 90
#     deltaheading = math.fabs(heading-heading2)
#     if deltaheading > 0.5:
#         acc+=1
#         print((heading,heading2))


#     A = StreetScanner([lon1,lat1], [lon2,lat2], length
#     , StreetName) #c1的经度维度，c2经度纬度，长度
#     A.get_url()
