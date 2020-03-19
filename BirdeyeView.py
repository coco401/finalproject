import numpy
import io
from math import sin,pi,log
zoom = 20
api_key = "AIzaSyCqes_Fi9KhIODy9nO0P-SDXlr_YPtzPeU"
center = "36.96573379953917,-122.0070526367014"
url = "http://maps.googleapis.com/maps/api/staticmap"
size = "640X640"
# def draw_image(image):
#     image_one = ImageTk.PhotoImage(Image.open(io.BytesIO(image)))
#     canvas.create_image(640, 640, image = image_one)
#     draw_car_trajectory()
#     links = url + "center=" + center + "&size=" +size + "&zoom=" + str(zoom) + "&maptype=satellite"  "&key=" + api_key + "&sensor=false&format=jpg-baseline&maptype=satellite"
#     r = requests.get(links)
#     r = requests.get(" ") 
#     # print(type(r.content))
#     draw_image(r.content)

def latToPixel(lat, zoom):
    siny = sin(lat * pi / 180)
    y = log((1 + siny) / (1 - siny))
    return (128 << zoom) * (1 - y / (2 * pi))
def lngToPixel(lng, zoom):
    return (lng + 180) * (256 << zoom) / 360

print(latToPixel(36.9655691959434,20))
print(latToPixel(36.9657496345902,20))
print(lngToPixel(-122.0063727717091,20))
print(lngToPixel(-122.0063608635011,20))
a = latToPixel(36.9655691959434,20) - latToPixel(36.9657496345902,20)
b = lngToPixel(-122.0063727717091,20) - lngToPixel(-122.0063608635011,20)
print(a)
print(b)


