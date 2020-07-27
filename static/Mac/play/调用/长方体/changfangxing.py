#第一种
import random
class cube:
    def define(self):
        global x,y,z
        x=self.x = random.randint(1,5)
        y=self.y = random.randint(1,5)
        z=self.z = random.randint(1,5)
        return x,y,z
    def Cuboid_Area(self):
        global Area
        Area=(2*(self.x * self.y + self.x * self.z + self.y * self.z))
        return Area
    def Cuboid_volume(self):
        global svolume
        svolume=(self.x*self.y*self.z)
        return svolume
class z_cobe(cube):
    def side(self):
        global a
        a=self.a=random.randint(1,5)
        return a
    def side_superficial_area(self):
        global cobe_area
        cobe_area=(6*(self.a**2))
        return cobe_area
    def cobe_volume(self):
        global vvlume
        vvlume=(self.a**3)
        return vvlume
ALL=cube()
ALL.define()
ALL.Cuboid_Area()
ALL.Cuboid_volume()
print(('the long of cube is ' + str(x)))
print(('the wide of cube is ' + str(y)))
print(('the high of cube is ' + str(z)))
print('the Cuboid_Area of cube is ' + str(Area))
print('the Cuboid_svolume of cube is ' + str(svolume))
all=z_cobe()
all.side()
all.side_superficial_area()
all.cobe_volume()
print()
print('the side_superficial_area of cube is ' + str(cobe_area))
print('the cobe_volume of cube is ' + str(vvlume))


#第二种
class Cube:
    def __init__(self,L,W,H):
        self.L = L
        self.W = W
        self.H = H
    def surface(self):
        global result1
        result1 = (L*W+W*H+H*L)*2
        return result1
    def volume(self):
        global result2
        result2 = L*W*H
        return result2
L = 2
W = 3
H = 4
a = Cube(L,W,H)
a.surface()
a.volume()
print ('the surface of cube is '+str(result1))
print ('the volume of cube is '+str(result2))

#第三种
class Cube:
    def __init__(self,l,w,h):
        self.l = l
        self.w = w
        self.h = h
    def surface(self):
        global result3
        result3 = (l*w+w*h+h*l)*2
        return result3
    def volume(self):
        global result4
        result4 = l*w*h
        return result4
l = int(input('长：'))
w = int(input('宽：'))
h = int(input('高：'))
a = Cube(l,w,h)
a.surface()
a.volume()
print ('the surface of cube is '+str(result3))
print ('the volume of cube is '+str(result4))