#! python2
# -*- coding:utf-8 -*-
import sys
import math
from math import sin, cos, sqrt, atan2, radians

from geopy.distance import geodesic
class CoordinateDistance(object):

    def calculateDIS(self,point_1_lat, point_1_lon, point_2_lat, point_2_lon, unit='m'):
        # approximate radius of earth in km
        R = 6371.009
        lat1 = radians(float(point_1_lat))
        lon1 = radians(float(point_1_lon))
        lat2 = radians(float(point_2_lat))
        lon2 = radians(float(point_2_lon))

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c * 1000
        print("Distance: " + str(distance) + "m")
        return distance
    def getDis(self,pointX,pointY,lineX1,lineY1,lineX2,lineY2,distance):
        a=lineY2-lineY1
        b=lineX1-lineX2
        c=lineX2*lineY1-lineX1*lineY2
        disptop = sqrt(a**2 + b**2)
        disptol=(math.fabs(a*pointX+b*pointY+c))/(sqrt(a**2+b**2))
        print(disptop)
        print(disptol)
        result = (disptol/disptop) * distance
        return result


if __name__ == '__main__':
    point_1_lat = 36.96573379953917
    print("Point 1 lat: " + str(point_1_lat))
    point_1_lon =  -122.0070526367014
    print("Point 1 lon: " + str(point_1_lon))
    point_2_lat =  36.96564353371734
    print("Point 2 lat: " + str(point_2_lat))
    point_2_lon = -122.0070467630012
    print("Point 2 lon: " + str(point_2_lon))
    A = CoordinateDistance()
    A.calculateDIS(point_1_lat,point_1_lon,point_2_lat,point_2_lon)
    distance = geodesic((point_1_lat, point_1_lon),(point_2_lat, point_2_lon)).meters
    heading = str(math.degrees(math.atan((point_2_lon - point_1_lon) / (point_2_lat - point_1_lat))) + 90)
    print(distance,heading)
    dis=A.getDis(370, 295, 300, 300, 306, 385, distance)   
    print(dis)

# 36.96536620751913_-122.0070287175351_85.82967837233797_FrontView
# 36.96545601823645_-122.0070345615883_85.82967837233797_FrontView
# 36.96536620751913__85.82967837233797_FrontView
# 36.96545601823645_-122.0070345615883_85.82967837233797_FrontView
