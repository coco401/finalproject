
import urllib.request
 

def download(url, name):
    # path = "C:\\Users\\Administrator\\Desktop\\pictures"
    #url = "http://pic2.sc.chinaz.com/files/pic/pic9/201309/apic520.jpg"
    #url = "https://maps.googleapis.com/maps/api/streetview?size=600x300&location=46.414382,10.013988&heading=151.78&pitch=-0.76&key="#你的KEY"

    conn = urllib.request.urlopen(url)
    f = open(name, 'wb')
    f.write(conn.read())
    f.close()
    print('Pic Saved!') 

center = "36.96536620751913,-122.0070287175351"
a = "36.96545601823645,-122.0070345615883"
b = "36.96582691646846,-122.0070586959411"
url= "https://maps.googleapis.com/maps/api/staticmap?center="\
+center+"&zoom=20&size=640x640&maptype=satellite&markers=color:blue%7Clabel:A%7C"\
+center+"&markers=color:green%7Clabel:B%7C"+ a +"&path=color:0x0000ff|weight:5|"+center+"|"+a+"&key=AIzaSyCqes_Fi9KhIODy9nO0P-SDXlr_YPtzPeU"
name = "C:\\Users\\Yang\\Desktop\\master project\\static.jpg"
download(url,name)