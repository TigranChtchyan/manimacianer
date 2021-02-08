from manimlib.imports import *
from erkr import *
import numpy as np

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
