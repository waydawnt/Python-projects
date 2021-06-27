tesh_h = int(input("Height of wall : "))
tesh_w = int(input("Width of wall :"))
coverage = 5

def paint_calc(height, width, cover) :
    no_of_cans = (height * width) / cover
    print(round(no_of_cans))

paint_calc(height = tesh_h, width = tesh_w, cover = coverage)