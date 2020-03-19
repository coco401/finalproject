#x坐标变换
# input  x,y  out put new x,y
import numpy as np
import cv2 as cv
from math import cos,sin,radians,tan,atan,degrees,atan2, asin,sqrt

# class p1top2():
door_height = 2.032

garage_height = 2.1336

# [-2.798125, 0.11343750000000086, 12.1]
# [-9.713291932979814, 0.11343750000000086, 15.129510512251684]
[-2.798125, 0.11343750000000086, 12.1]
[0.5058162919401767, 0.11343750000000086, 14.263909686701103]

class P1toP2():
    '''
    输入的是A的像素(x,y), depth, pitch, BtoA
    '''
    def __init__(self, depth, BtoA, pitch):
        self.A_z = depth
        self.pitch = pitch
        self.BtoA = BtoA #shuru 时候已经变换过了
        # if pitch > 0:
        #     self.BtoA = -BtoA
        # elif pitch < 0:
        #     self.BtoA = BtoA

    def trans(self, P1):
        
        #zhijie
        A_X, A_Y = P1
        pitch = radians(self.pitch)
        A_x = (A_X * self.A_z -320*self.A_z)/320
        A_y = (A_Y * self.A_z -320*self.A_z)/320
        ax = 320 * (cos(pitch)*A_x - sin(pitch)*self.A_z  +cos(pitch)*(self.BtoA))/(sin(pitch)*A_x +cos(pitch)*self.A_z + sin(pitch)*(self.BtoA)) +320
        ay = 320 * (A_y / (sin(pitch)*A_x +cos(pitch)*self.A_z + sin(pitch)*(self.BtoA))) + 320
        return [round(ax), round(ay)]





        k = np.array([[320,0,320],[0,320,320],[0,0,1]])
        A_X, A_Y = P1
        A_x = (A_X * self.A_z -320* self.A_z)/320
        A_y = (A_Y * self.A_z -320* self.A_z)/320

        # A_z = 320 * A_y / (deltaA_Y) 


        p1 = [A_x,A_y,self.A_z]
        print(p1)

        pitch = radians(self.pitch)

        R = [[ cos(pitch), 0,  -sin(pitch)],
            [  0,         1,  0],
            [sin(pitch),  0,  cos(pitch)]]

        T = [cos(pitch)*(self.BtoA), 0, sin(pitch)*( self.BtoA)]   #T需要平移的是世界坐标系原点再相机坐标系下的坐标
        p2= np.dot(R,p1) + T

        P2 = np.dot(k,p2)
        P2 = P2/ P2[2]
        P2 = [int(P2[0]+0.5),int(P2[1]+0.5)]

        return P2

if __name__ =="__main__":
    
    AtoB = 10.5
    AtoC = 10.3
    depth = 11.4
    
    points = [[246, 323], [271, 321], [272, 380], [246, 380]]
    img = cv.imread("new0.jpg")
    cv.polylines(img, [np.int32(points)], isClosed=True, color=(0,0,255), thickness=1)
    cv.imshow("image", img)
    cv.waitKey(0)
    
  


    res = []
    A = P1toP2(depth,AtoB,-15)
    for i in points:
        res.append(A.trans(i))

    img = cv.imread("new-15.jpg")
    print(res)
    cv.polylines(img, [np.int32(res)], isClosed=True, color=(0,0,255), thickness=1)
    cv.imshow("image", img)
    cv.waitKey(0)

    res = []
    A = P1toP2(depth,AtoB,-30)
    for i in points:
        res.append(A.trans(i))

    img = cv.imread("new-30.jpg")

    cv.polylines(img, [np.int32(res)], isClosed=True, color=(0,0,255), thickness=1)
    cv.imshow("image", img)
    cv.waitKey(0)

    res = []
    A = P1toP2(depth,AtoC,15)
    for i in points:
        res.append(A.trans(i))

    img = cv.imread("new15.jpg")
    cv.polylines(img, [np.int32(res)], isClosed=True, color=(0,0,255), thickness=1)
    cv.imshow("image", img)
    cv.waitKey(0)
    
    res = []
    A = P1toP2(depth,AtoC,30)

    for i in points:
        p2 = A.trans(i)
        res.append(p2)
    img = cv.imread("new30.jpg")
    cv.polylines(img, [np.int32(res)], isClosed=True, color=(0,0,255), thickness=1)
    cv.imshow("image", img)
    cv.waitKey(0)