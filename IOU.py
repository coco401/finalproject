
import shapely
import numpy as np
from shapely.geometry import Polygon, MultiPoint  # 多边形
 
def bbox_iou_eval(box1, box2):
    '''
    利用python的库函数实现非矩形的IoU计算
    :param box1: list,检测框的四个坐标[x1,y1,x2,y2,x3,y3,x4,y4]
    :param box2: lsit,检测框的四个坐标[x1,y1,x2,y2,x3,y3,x4,y4]
    :return: IoU
    '''
    box1 = np.array(box1).reshape(4, 2)  # 四边形二维坐标表示
    # python四边形对象，会自动计算四个点，并将四个点重新排列成
    # 左上，左下，右下，右上，左上（没错左上排了两遍）
    poly1 = Polygon(box1).convex_hull
    box2 = np.array(box2).reshape(4, 2)
    poly2 = Polygon(box2).convex_hull
 
    if not poly1.intersects(poly2):  # 如果两四边形不相交
        iou = 0
    else:
        try:
            inter_area = poly1.intersection(poly2).area  # 相交面积
            iou = float(inter_area) / (poly1.area + poly2.area - inter_area)
        except shapely.geos.TopologicalError:
            print('shapely.geos.TopologicalError occured, iou set to 0')
            iou = 0
 
    return iou
 
if __name__ == '__main__':
    # box = [四个点的坐标，顺序无所谓]
    box3 = [10, 0, 15, 0, 15, 10, 10, 10]   # 左上，右上，右下，左下
    box4 = [12, 5, 20, 2, 20, 15, 12, 15]
    iou = bbox_iou_eval(box3, box4)
    print(iou)
