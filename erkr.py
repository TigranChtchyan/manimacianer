from manimlib.imports import *
from Useful_Funtions import *
from Grid_Funtions import *
import numpy as np

def segment_M(A,B):
	'''A և B կետերի միջնակետը
	type: Dot'''
	dot=Dot((A.get_center()+B.get_center())/2)
	return dot

def kentron(Circle):
	'''Circle շրջանագծի կենտրոնը
	type: Dot'''
	dot=Dot(Circle.get_center())
	return dot

def ughimq(A,B,C):
	'''A կետից BC ուղղին տարված ուղղահայաի հիմքը
	type: Dot'''
	ba=A.get_center()-B.get_center()
	bc=C.get_center()-B.get_center()
	n=sum(bc**2)
	proj=(np.dot(ba,bc)/n)*bc
	H=Dot(B.get_center()+proj)
	return H

def CirclePoint(Circle, phi):
	'''Circle շրջանագծի այն կետը, որը կենտրոնի նկատմամբ phi անկյան տակ է
	type: Dot'''
	width=Circle.get_width()
	dot=Dot(Circle.get_center()+width/2*np.sin(phi)*UP+width/2*np.cos(phi)*RIGHT)
	return dot

def ankyun(O,A):
	'''OA վեկտորի կազմած անկյունը {1,0} նկատմամբ
	'''
	x0=O.get_x()
	y0=O.get_y()
	x1=A.get_x()
	y1=A.get_y()
	#phia
	if(x1>x0 and y1>=y0):
		if(y1==y0):
			phia=0
		else:
			phia=np.arctan((y1-y0)/(x1-x0))
	elif(x1>0 and y1<y0):
		phia=2*PI+np.arctan((y1-y0)/(x1-x0))
	elif(x1==x0):
		if(y1>y0):
			phia=PI/2
		else:
			phia=3*PI/2
	else:
		phia=PI-np.arctan((y1-y0)/(x0-x1))
	return phia

def line_intersect(A1,A2,B1,B2):
    '''A1A2 B1B2 ուղիղների հատման կետը
    type: Dot'''
    Ax1=A1.get_x()
    Ay1=A1.get_y()
    Ax2=A2.get_x()
    Ay2=A2.get_y()
    Bx1=B1.get_x()
    By1=B1.get_y()
    Bx2=B2.get_x()
    By2=B2.get_y()
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return False
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)

    dot=Dot(x*RIGHT+y*UP)
    return dot

def distance(A,B):
	'''A և B կետերի հեռավորությունը
	type: number
	Warning: Միգուցե բավարար Ճշգրիտ չի
	'''
	x1=A.get_x()
	x2=B.get_x()
	y1=A.get_y()
	y2=A.get_y()
	distance=(x2-x1)**2+(y2-y1)**2
	distance=distance**0.5
	return distance

#ankax functianer

# ankyun
# ABC անկյունը նշել մի գծով
def angle(A, B, C, radius):
	phia=ankyun(B,A)
	phic=ankyun(B,C)
	if(phic>=phia):
		if(phic-phia>PI):
			arc=Arc(phia, phic-phia-2*PI)
		else:
			arc=Arc(phia, phic-phia)
	else:
		if(phia-phic>PI):
			arc=Arc(phic, phia-phic-2*PI)
		else:
			arc=Arc(phic, phia-phic)
	arc.set_width(2*radius)
	T=B.get_center()
	arc.move_arc_center_to(T)
	return arc

# segment_M, ankyun, kentron, CirclePoint, 
# Circle շրջանագծի վրա AB փոքր աղեղի միջնակետը
def arc_M(Circle, A,B):
	T=segment_M(A,B)
	if(Circle.get_center().any()!=T.get_center().any()):
		phi=ankyun(kentron(Circle),T)
		M=CirclePoint(Circle, phi)
		return M
	else:
		phi=ankyun(kentron(Circle),A)
		M=CirclePoint(Circle, phi+PI/2)
		return M

# ankyun
# ABC անկյան արժեքը
def ank(A,B,C):
	phia=ankyun(B,A)
	phic=ankyun(B,C)
	if(phic>=phia):
		if(phic-phia>PI):
			return (phia+2*PI-phic)
		else:
			return phic-phia
	else:
		if(phia-phic>PI):
			return phic-phia+2*PI
		else:
			return phia-phic

def kis(A,B,C):
	return A

def qar(A,H,B,koghm):
	phia=ankyun(H,A)
	phib=ankyun(H,B)
	W=Circle()
	W.set_width(2*koghm)
	W.move_to(H)
	A1=CirclePoint(W,phia)
	B1=CirclePoint(W,phib)
	coord=A1.get_center()-H.get_center()+B1.get_center()
	H1=Dot(coord)
	l1=Line(A1.get_center(),H.get_center())
	l2=Line(A1.get_center(),H1.get_center())
	l3=Line(H.get_center(),B1.get_center())
	l4=Line(H1.get_center(),B1.get_center())
	group=VGroup(l1,l2,l3,l4)
	return group
