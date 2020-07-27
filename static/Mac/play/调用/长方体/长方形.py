class oblong:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def oblong_girth(self):
        global lw
        lw=(l+w)*2
        return lw
    def oblong_area(self):
        global l_w
        l_w = l*w
        return l_w
class square(oblong):
    def __init__(self,l,w):
        if l==w:
            oblong.__init__(self,l,w)
    def square_girth(self):
        global bb
        bb = 4*l
        return bb
    def square_area(self):
        global b_b
        b_b = l*l
        return b_b

l = int(input('长：'))
w = int(input('宽：'))
长方形=oblong(l,w)
长方形.oblong_girth()
长方形.oblong_area()
正方形=square(l,w)
正方形.square_girth()
正方形.square_area()
print ('the oblong_girth of cube is '+str(lw),end=' ')
print ('the oblong_area of cube is '+str(l_w))

print ('the square_girth of cube is '+str(bb),end=' ')
print ('the square_area of cube is '+str(b_b))