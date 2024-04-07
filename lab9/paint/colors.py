colorBLACK = (0, 0, 0) 
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)
colorCYAN = (0, 255,255)
colorBROWN = (153, 76, 0)
color_list = [colorBLACK, colorBLUE, colorGREEN, colorRED, colorYELLOW, colorCYAN, colorBROWN, colorWHITE]
color_index = 0
color_current = color_list[color_index]

def next_color():
    global color_index, color_current, color_list
    color_index = (color_index+1)%len(color_list)
    return color_list[color_index]