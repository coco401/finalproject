# coding: utf-8
import cv2
import numpy as np

img = cv2.imread("static.jpg")
#print img.shape

pts = []

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    global pts
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        print(xy)
        pts.append([x,y])
        print(pts)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness = -1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (255,0,0), thickness = 1)
        if len(pts) == 4:
            print(pts)
            pt = np.int32(pts)
            cv2.polylines(img, [np.int32(pt)], isClosed=True, color=(0,0,255), thickness=1)
            pts = []
        cv2.imshow("image", img)
        
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

cv2.imshow("image", img)

# while(True):
#     try:
#         cv2.waitKey(100)

#     except Exception:
#         cv2.destroyWindow("image")
#         break
        
cv2.waitKey(0)

cv2.imshow("image", img)
cv2.destroyAllWindow()
