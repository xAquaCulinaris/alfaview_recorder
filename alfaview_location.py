from ewmh import EWMH
import time
ewmh = EWMH()

def get_alfaview_location():
    alfaview_geometry = ewmh.getActiveWindow().query_tree().parent.get_geometry()
    x = alfaview_geometry.x
    y = alfaview_geometry.y
    width = alfaview_geometry.width
    height = alfaview_geometry.height
    return(x,y,width,height)
