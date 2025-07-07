def area_tri(base,altura):
    if type(base) == str or type(altura) == str:
        return 0
    area =(base*altura)/2
    return area
area3 = area_tri("a","6")
print(area3)
area1 = area_tri(10,15)
print(area1)
area2 = area_tri(20,25)
print(area2)