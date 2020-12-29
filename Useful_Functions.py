# Այստեղ կան կյանքը հեշտացնող ֆունկցիաներ, որոնք
# կարելի է օգտագործել տարբեր իրավիճակներում:

from manimlib.imports import *
import numpy as np

#vdaaaaaaaaaa
def vernagir(header):
	lin=Line(5*LEFT, 5*RIGHT)
	vern=VGroup(header, lin)
	vern.arrange(DOWN)
	vern.to_edge(UP)
	return vern
  
#ervrrrrrrrrre
def qarakusikner(w,n,color):
	x=Square(color=color)
	x.set_width(w)
	for i in range(1,n):
		s=Square(color=color)
		s.set_width(w)
		s.shift((i*w)*RIGHT)
		x=VGroup(x, s)
	x.shift((n-1)*w*0.5*LEFT)
	return x
  
#vsdddddddddddddddddd
def aghyusak(w, togh, syun, color):
	t=(qarakusikner(w, syun, color))
	a=t
	for i in range(1,togh):
		s=a.copy()
		s.shift((i*w)*UP)
		t=VGroup(t, s)
	t.shift((togh-1)*w*0.5*DOWN)
	return t
