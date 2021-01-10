from manimlib.imports import *
import numpy as np

# +Այս ֆունկցիան Circle շրջանագծի վրա առանձնացնում է այն կետը,
# որը կենտրոնի նկատմամբ phi անկյան տակ է 
def CirclePoint(Circle, phi):
	width=Circle.get_width()
	dot=Dot(Circle.get_center()+width/2*np.sin(phi)*UP+width/2*np.cos(phi)*RIGHT)
	return dot

# +A և B կետերի միջնակետը
def segment_M(A,B):
	dot=Dot((A.get_center()+B.get_center())/2)
	return dot

# +Շրջանագծի կենտրոնը
def kentron(Circle):
	dot=Dot(Circle.get_center())
	return dot

# +A կետի անկյունը O կետի նկատմամբ
#	tas=10*13
#	x0=int(O.get_x()*tas)
#	y0=int(O.get_y()*tas)
#	x1=int(A.get_x()*tas)
#	y1=int(A.get_y()*tas)
#	x0/=tas
#	y0/=tas
#	x1/=tas
#	y1/=tas
def ankyun(O,A):
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

# Ճշգրության պակաս եմ զգում
# +A և B կետերի հեռավորությունը
def distance(A,B):
	x1=A.get_x()
	x2=B.get_x()
	y1=A.get_y()
	y2=A.get_y()
	distance=(x2-x1)**2+(y2-y1)**2
	distance=distance**0.5
	return distance

# +A կետից BC ուղղին տարված ուղղահայաի հիմքը
def ughhimq(A,B,C):
	ba=A.get_center()-B.get_center()
	bc=C.get_center()-B.get_center()
	n=sum(bc**2)
	proj=(np.dot(ba,bc)/n)*bc
	H=Dot(B.get_center()+proj)
	return H

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

def qar(A,H,B, koghm):
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

def line_intersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    """ returns a (x, y) tuple or None if there is no intersection """
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

class er(Scene):
	def construct(self):
		W=Circle()
		W.set_width(6)
		W.set_color(WHITE)
		kent=kentron(W)

		A=CirclePoint(W, 6*PI/5)
		B=CirclePoint(W, 5*PI/8)
		C=CirclePoint(W, 9*TAU/10)
		A.set_color(BLUE)
		B.set_color(BLUE)
		C.set_color(BLUE)

		a=Line(B,C)
		b=Line(A,C)
		c=Line(B,A)
		self.play(ShowCreation(W))
		self.play(ShowCreation(A), ShowCreation(B), ShowCreation(C))
		self.wait()
		self.play(ShowCreation(a), ShowCreation(b), ShowCreation(c))
		self.wait()

		vertA=TexMobject("A")
		vertB=TexMobject("B")
		vertC=TexMobject("C")
		vertA.next_to(A, LEFT)
		vertB.next_to(B, UP)
		vertC.next_to(C, RIGHT)

		self.play(Write(vertA), Write(vertB), Write(vertC))
		self.wait()

		B1=arc_M(W,A,C)
		b1=Line(B,B1)
		C1=arc_M(W,A,B)
		c1=Line(C,C1)
		A1=arc_M(W,B,C)
		a1=Line(A,A1)
		self.play(Write(B1),Write(C1),Write(A1))
		self.play(ShowCreation(a1),ShowCreation(b1),ShowCreation(c1))
		self.wait()
		I=line_intersect(B.get_x(),B.get_y(),B1.get_x(),B1.get_y(),A.get_x(),A.get_y(),A1.get_x(),A1.get_y())
		self.play(FadeIn(I))
		self.wait()
class f_check(Scene):
	def construct(self):
		O=Circle()
		O.set_width(6)
		O.set_color(WHITE)
		kent=kentron(O)

		A=CirclePoint(O, PI)
		B=CirclePoint(O, 5*PI/8)
		C=CirclePoint(O, 0)
		A.set_color(BLUE)
		B.set_color(BLUE)
		C.set_color(BLUE)

		a=Line(B,C)
		b=Line(A,C)
		c=Line(B,A)
		self.play(ShowCreation(O))
		self.play(ShowCreation(A), ShowCreation(B), ShowCreation(C))
		self.wait()
		self.play(ShowCreation(a), ShowCreation(b), ShowCreation(c))
		self.wait()

		k=arc_M(O, B,C)
		self.play(GrowFromCenter(k))

class projetion(Scene):
	def construct(self):
		O=Circle()
		O.set_width(6)
		O.set_color(WHITE)
		kent=kentron(O)

		A=CirclePoint(O, PI*6/5)
		B=CirclePoint(O, 5*PI/8)
		C=CirclePoint(O, 9*TAU/10)

class functions(Scene):
	def altitudes(self,A,B,C):
		A1=ughhimq(A,B,C)
		B1=ughhimq(B,C,A)
		C1=ughhimq(C,A,B)
		return [Line(A,A1),Line(B,B1),Line(C,C1)]
	def construct(self):
		O=Circle()
		O.set_width(6)
		O.set_color(WHITE)
		kent=kentron(O)

		A=CirclePoint(O, 6*PI/5)
		B=CirclePoint(O, 5*PI/8)
		C=CirclePoint(O, 9*TAU/10)

		a=Line(B,C)
		b=Line(A,C)
		c=Line(B,A)
		self.play(ShowCreation(O))
		self.play(ShowCreation(A), ShowCreation(B), ShowCreation(C))
		self.wait()
		self.play(ShowCreation(a), ShowCreation(b), ShowCreation(c))
		self.wait()

		k=self.altitudes(A,B,C)
		self.play(Write(k[0]),Write(k[1]),Write(k[2]))
		self.play()
