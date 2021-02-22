from ewmh import EWMH

ewmh = EWMH()

def get_alfaview_location():
    alfaview_geometry = ewmh.getActiveWindow().query_tree().parent.get_geometry()
    x = alfaview_geometry.x
    y = alfaview_geometry.y
    width = alfaview_geometry.width
    height = alfaview_geometry.height
    print("Alfaview window: x=" + str(x) + " y=" + str(y) + " w=" + str(width) + " h=" + str(height))

    return(y,x,width,height)
