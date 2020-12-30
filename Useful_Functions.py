# Այստեղ կան կյանքը հեշտացնող ֆունկցիաներ, որոնք
# կարելի է օգտագործել տարբեր իրավիճակներում:

from manimlib.imports import *
import numpy as np

# Այս ֆունկցիան վերադարձնում է վերնագիրը էջի վերևում և դրա տակը գիծ քաշած
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
	t=qarakusikner(width, syun, color)
	a=t
	for i in range(1,togh):
		s=a.copy()
		s.shift((i*width)*UP)
		t=VGroup(t, s)
	t.shift((togh-1)*width*0.5*DOWN)
	return t

# Այս ֆունկցիան վերադարձնում է width երկարությամբ կողմ ունեցող և color գույն ունեցող
# կողք կողքի շարված n հատ քառակուսիկների Array, որի կենտրոնը (0,0) կետն է
def qar_array(width,n,color):
	x=Square(color=color)
	x.set_width(width)
	t=[]
	for i in range(n):
		s=x.copy()
		s.shift((i*width)*RIGHT)
		t.append(s)
		t[i].shift((n-1)*width*0.5*LEFT)
	return t

# Այս ֆունկցիան վերադարձնում է width երկարությամբ կողմ ունեցող և color գույն ունեցող
# կողք կողքի շարված n հատ քառակուսիկների Array, որի կենտրոնը (0,0) կետն է և որոնք midtogh հեռավորությամբ են
def qar_array_2(width,n,color,midtogh):
	x=Square(color=color)
	x.set_width(width)
	t=[]
	for i in range(n):
		s=x.copy()
		s.shift((i*(width+midtogh))*RIGHT)
		t.append(s)
		t[i].shift((n-1)*(width+midtogh)*0.5*LEFT)
	return t

# Այս ֆունկցիան վերադարձնում է width երկարությամբ կողմ ունեցող և color գույն ունեցող
# togh*syun աղյուսակի տեսքով շարված քառակուսիկների Array, որի կենտրոնը (0,0) կետն է
def agh_array(width, togh, syun, color):
	t=qar_array(width, syun, color)
	k=[]
	for i in range(togh):
		s=qar_array(width, syun, color)
		for j in range(syun):
			s[j].shift((i*width)*UP)
			s[j].shift((togh-1)*width*0.5*DOWN)
		k.append(s)
	return k

# Այս ֆունկցիան վերադարձնում է width երկարությամբ կողմ ունեցող և color գույն ունեցող
# togh*syun աղյուսակի տեսքով շարված քառակուսիկների Array, որի կենտրոնը (0,0) կետն է, և որոնք ունեն midtogh ու midsyun հեռավորությունները
def agh_array_2(width, togh, syun, color, midtogh, midsyun):
	k=[]
	for i in range(togh):
		s=qar_array_2(width, syun, color, midtogh)
		for j in range(syun):
			s[j].shift((i*(width+midsyun)*UP))
			s[j].shift((togh-1)*(width+midsyun)*0.5*DOWN)
		k.append(s)
	return k

# Այս ֆունկցիան Circle շրջանագծի վրա առանձնացնում է այն կետը,
# որը կենտրոնիի նկատմամբ phi անկյան տակ է 
def CirclePoint(Circle, phi):
	width=Circle.get_width()
	dot=Dot(Circle.get_center()+width/2*np.sin(phi)*UP+width/2*np.cos(phi)*RIGHT)
	return dot
