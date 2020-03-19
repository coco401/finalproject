import json
import numpy as np
import pandas as pd
from geopy.distance import geodesic
import os
import urllib.request
from test2 import p1top2
from test3 import P1toP2
import cv2 as cv
from math import sin,cos,pi,log,radians

def normaltocylindrical(i):
    f =320
    inew = f * np.arctan((i-320)/f) + 320
    return inew

def download(url, name):
    conn = urllib.request.urlopen(url)
    f = open(name, 'wb')
    f.write(conn.read())
    f.close()
    print('Pic Saved!') 

def latToPixel(lat, zoom):
    lat = float(lat)
    siny = sin(lat * pi / 180)
    y = log((1 + siny) / (1 - siny))
    return (128 << zoom) * (1 - y / (2 * pi))

def lngToPixel(lng, zoom):
    lng = float(lng)
    return (lng + 180) * (256 << zoom) / 360
with open('export-2020-01-09T04_24_26.335Z.json') as f:
    data = json.load(f)


#按坐标排序
for i in range(len(data)-1):
    for j in range(len(data)-1):
        point_0_lat,point_0_lon,view,_ = data[j]['External ID'].split('_')
        point_2_lat,point_2_lon,view,_ = data[j+1]['External ID'].split('_')
        if point_0_lat > point_2_lat:
            data[j],data[j+1] = data[j+1],data[j]


for i in range(len(data)):
    if data[i]['Label'] == 'Skip':
        continue

    else:

        point_0_lat,point_0_lon,view,_ = data[i]['External ID'].split('_')
        if i>0 and i<len(data):
            point_1_lat,point_1_lon,view_1,_ = data[i-1]['External ID'].split('_')
            point_2_lat,point_2_lon,view_2,_ = data[i+1]['External ID'].split('_')

            distance1 = geodesic((point_0_lat, point_0_lon),(point_1_lat, point_1_lon)).meters
            distance2 = geodesic((point_0_lat, point_0_lon),(point_2_lat, point_2_lon)).meters

            view1 = float(view) + 15
            view2 = float(view) + 30
            view3 = float(view) - 15
            view4 = float(view) - 30

            url1 = "https://maps.googleapis.com/maps/api/streetview?size=640x640&location=" + point_2_lat + "," + point_2_lon + "&heading=" + str(view1) + "&key=AIzaSyCC_bzL68dKT0ha3pqvB4Q_1Hk75nU5TvQ"
            url2 = "https://maps.googleapis.com/maps/api/streetview?size=640x640&location=" + point_2_lat + "," + point_2_lon + "&heading=" + str(view2) + "&key=AIzaSyCC_bzL68dKT0ha3pqvB4Q_1Hk75nU5TvQ"
            url3 = "https://maps.googleapis.com/maps/api/streetview?size=640x640&location=" + point_1_lat + "," + point_1_lon + "&heading=" + str(view3) + "&key=AIzaSyCC_bzL68dKT0ha3pqvB4Q_1Hk75nU5TvQ"
            url4 = "https://maps.googleapis.com/maps/api/streetview?size=640x640&location=" + point_1_lat + "," + point_1_lon + "&heading=" + str(view4) + "&key=AIzaSyCC_bzL68dKT0ha3pqvB4Q_1Hk75nU5TvQ"
            
            birdeyeurl = "http://maps.googleapis.com/maps/api/staticmap?size=640x640&maptype=satellite&zoom=20" + "&center=" + point_0_lat +"," + point_0_lon + \
            "&markers=color:blue%7Clabel:A%7C" + point_0_lat + "," + point_0_lon + "&markers=color:blue%7Clabel:B%7C" + point_1_lat + "," + point_1_lon + \
            "&markers=color:blue%7Clabel:C%7C" + point_2_lat + "," + point_2_lon + \
            "&key=AIzaSyCqes_Fi9KhIODy9nO0P-SDXlr_YPtzPeU" 
            
            name0 = "C:\\Users\\Yang\\Desktop\\master project\\pictures\\2nd Avenue\\" + "2nd Avenue_"+ point_0_lat + "_" + point_0_lon + "_" + str(view) + "_FrontView.JPG"

            name1 = "C:\\Users\\Yang\\Desktop\\master project\\test2ave\\" + point_2_lat + "_" + point_2_lon + "_" + str(view1) + "_15view.JPG"
            name2 = "C:\\Users\\Yang\\Desktop\\master project\\test2ave\\" + point_2_lat + "_" + point_2_lon + "_" + str(view2) + "_30view.JPG"
            name3 = "C:\\Users\\Yang\\Desktop\\master project\\test2ave\\" + point_1_lat + "_" + point_1_lon + "_" + str(view3) + "_-15view.JPG"
            name4 = "C:\\Users\\Yang\\Desktop\\master project\\test2ave\\" + point_1_lat + "_" + point_1_lon + "_" + str(view4) + "_-30view.JPG"

            birdeyename = "C:\\Users\\Yang\\Desktop\\master project\\test2ave\\" + point_0_lat + "_" + point_0_lon + "_birdeye.JPG"

            # download(url1, name1)
            # download(url2, name2)
            # download(url3, name3)
            # download(url4, name4)

            # download(birdeyeurl, birdeyename)

            img1 = cv.imread(name1)
            img2 = cv.imread(name2)
            img3 = cv.imread(name3)
            img4 = cv.imread(name4)
            
            # imgbird = cv.imread(birdeyename)
            
            y1 = round(latToPixel(point_1_lat,20) - latToPixel(point_0_lat,20) +320 )
            x1 = round(lngToPixel(point_1_lon,20) - lngToPixel(point_0_lon,20) +320)

            y2 = round(latToPixel(point_2_lat,20) - latToPixel(point_0_lat,20) +320)
            x2 = round(lngToPixel(point_2_lon,20) - lngToPixel(point_0_lon,20) +320)
            
            view = radians(float(view))

            print("view")
            print([x1,y1])
            print([point_1_lon,point_0_lon])

            x1_15 = round(x1 + 100 * sin(radians(view3)))
            y1_15 = round(y1 - 100 * cos(radians(view3)))

            x1_30 = round(x1 + 100 * sin(radians(view4)))
            y1_30 = round(y1 - 100 * cos(radians(view4)))

            x2_15 = round(x2 + 100 * sin(radians(view1)))
            y2_15 = round(y2 - 100 * cos(radians(view1)))

            x2_30 = round(x2 + 100 * sin(radians(view2)))
            y2_30 = round(y2 - 100 * cos(radians(view2)))

            x_0 = round(320 + 100 * sin(view))
            y_0 = round(320 - 100 * cos(view))
            
            color = (0, 255, 0) 
            thickness = 4

            # imgbird = cv.arrowedLine(imgbird,(320,320),(x_0,y_0),(255,255,255),4)
            # imgbird = cv.arrowedLine(imgbird,(x1,y1),(x1_15,y1_15),(255,0,0),4)
            # imgbird = cv.arrowedLine(imgbird,(x1,y1),(x1_30,y1_30),(0,255,0),4)

            # imgbird = cv.arrowedLine(imgbird,(x2,y2),(x2_15,y2_15),(255,0,0),4)
            # imgbird = cv.arrowedLine(imgbird,(x2,y2),(x2_30,y2_30),(0,255,0),4)

            # cv.imwrite(birdeyename,imgbird)
     

            img0 = cv.imread(name0)

            height = 2.032
            depths = []
            for j in data[i]['Label']['door']:
                points = []
                for k in j['geometry']:
                    point=[k['x'],k['y']]
                    points.append(point)
                print(points)
                tall = abs(points[0][1]-points[2][1])
                depth = height*320/tall
                depths.append(depth)
            
            print("depths"+str(depths))
            # tall = abs(points[0][1]-points[2][1])
            # depth = height*320/tall
            # print(depth) 

            # A = P1toP2(depth,-distance1,-15)
            # B = P1toP2(depth,-distance1,-30)
            # C = P1toP2(depth,distance2,15)
            # D = P1toP2(depth,distance2,30)

            
            for j in data[i]['Label']['door']:
                print(j['geometry'])
                depth = depths.pop(0)

                A = P1toP2(depth,-distance1,-15)
                B = P1toP2(depth,-distance1,-30)
                C = P1toP2(depth,distance2,15)
                D = P1toP2(depth,distance2,30)
                res1 = []
                res2 = []
                res3 = []
                res4 = []
                points = []
                
                for k in j['geometry']:
                    point=[k['x'],k['y']]
                   

                    res3.append(A.trans(point))
                    res4.append(B.trans(point))

                    res1.append(C.trans(point))
                    res2.append(D.trans(point))

                    points.append(point)

                cv.polylines(img0, [np.int32(points)], isClosed=True, color=(0,0,255), thickness=1)
                cv.polylines(img1, [np.int32(res1)], isClosed=True, color=(0,0,255), thickness=1)
                cv.polylines(img2, [np.int32(res2)], isClosed=True, color=(0,0,255), thickness=1)
                cv.polylines(img3, [np.int32(res3)], isClosed=True, color=(0,0,255), thickness=1)
                cv.polylines(img4, [np.int32(res4)], isClosed=True, color=(0,0,255), thickness=1)

            cv.imshow("image", img0)
            cv.waitKey(0)
            
            
            cv.imshow("image", img1)
            cv.waitKey(0)
            
            cv.imshow("image", img2)
            cv.waitKey(0)
            
            cv.imshow("image", img3)
            cv.waitKey(0)
            cv.imshow("image", img4)
            cv.waitKey(0)
            img5 = np.zeros((640,640,3), np.uint8)  
            
            img5.fill(255)
            


            name0 = "C:\\Users\\Yang\\Desktop\\master project\\resultspics\\" + str(i) + "_0.JPG"
            name1 = "C:\\Users\\Yang\\Desktop\\master project\\resultspics\\" + str(i) + "_15view.JPG"
            name2 = "C:\\Users\\Yang\\Desktop\\master project\\resultspics\\" + str(i) + "_30view.JPG"
            name3 = "C:\\Users\\Yang\\Desktop\\master project\\resultspics\\" + str(i) + "_-15view.JPG"
            name4 = "C:\\Users\\Yang\\Desktop\\master project\\resultspics\\" + str(i) + "_-30view.JPG"
            name5 = "C:\\Users\\Yang\\Desktop\\master project\\resultspics\\" + str(i) + "_blank.JPG"
            cv.imwrite(name0,img0)
            cv.imwrite(name1,img1)
            cv.imwrite(name2,img2)
            cv.imwrite(name3,img3)
            cv.imwrite(name4,img4)
            # cv.imwrite(name5,imgbird)

                









        


        # for j in data[i]['Label']['door']:

        #     print(j['geometry'])


