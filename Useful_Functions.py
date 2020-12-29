# Այստեղ կան կյանքը հեշտացնող ֆունկցիաներ, որոնք
# կարելի է օգտագործել տարբեր իրավիճակներում:

from manimlib.imports import *
import numpy as np

# Այս ֆունկցիան վերադարձնում է
def vernagir(header):
	lin=Line(5*LEFT, 5*RIGHT)
	vern=VGroup(header, lin)
	vern.arrange(DOWN)
	vern.to_edge(UP)
	return vern
  
# Այս ֆունկցիան վերադարձնում է width երկարությամբ կողմ ունեցող և color գույն ունեցող
# կողք կողքի շարված n հատ քառակուսիկների Group, որի կենտրոնը (0,0) կետն է
def qarakusikner(width,n,color):
	x=Square(color=color)
	x.set_width(width)
	for i in range(1,n):
		s=Square(color=color)
		s.set_width(width)
		s.shift((i*width)*RIGHT)
		x=VGroup(x, s)
	x.shift((n-1)*width*0.5*LEFT)
	return x

# Այս ֆունկցիան վերադարձնում է width երկարությամբ կողմ ունեցող և color գույն ունեցող
# togh*syun աղյուսակի տեսքով շարված քառակուսիկների Group, որի կենտրոնը (0,0) կետն է
def aghyusak(width, togh, syun, color):
	t=(qarakusikner(width, syun, color))
	a=t.copy()
	for i in range(1,togh):
		s=a.copy()
		s.shift((i*width)*UP)
		t=VGroup(t, s)
	t.shift((togh-1)*width*0.5*DOWN)
	return t
