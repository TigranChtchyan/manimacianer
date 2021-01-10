from manimlib.imports import *
import numpy as np

# Grid functions
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
def qarakusikner_2(width,n,color,midtogh):
	t=qar_array_2(width,n,color,midtogh)
	x=t[0]
	for i in range(1,len(t)):
		x=VGroup(x,t[i])
	return x

def aghyusak(width, togh, syun, color):
	t=qarakusikner(width, syun, color)
	a=t
	for i in range(1,togh):
		s=a.copy()
		s.shift((i*width)*UP)
		t=VGroup(t, s)
	t.shift((togh-1)*width*0.5*DOWN)
	return t
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
def agh_array_2(width, togh, syun, color, midtogh, midsyun):
	k=[]
	for i in range(togh):
		s=qar_array_2(width, syun, color, midtogh)
		for j in range(syun):
			s[j].shift((i*(width+midsyun)*UP))
			s[j].shift((togh-1)*(width+midsyun)*0.5*DOWN)
		k.append(s)
	return k
def aghyusak_2(width, togh, syun, color, midtogh, midsyun):
	k=agh_array_2(width, togh, syun, color, midtogh, midsyun)
	x=k[0][0]
	for i in range(len(k)):
		for j in range(len(k[0])):
			if(i!=0 or j!=0):
				x=VGroup(x,k[i][j])
	return x

class qar(Scene):
	def construct(self):
		s=Square(fill_color=GREEN)
		s.set_color(GREEN)
		s.shift(3.5*RIGHT)
		s.set_opacity(1)
		s.set_width(1)
		self.play(ShowCreation(s))
		self.wait()

		x1=TextMobject("1")
		x1.set_color(BLUE)
		x2=x1.copy()
		x1.next_to(s, RIGHT)
		x2.next_to(s, UP)
		self.play(Write(x1))
		self.play(Write(x2))
		self.wait()

		r=Rectangle(width=4, height=3)
		r.shift(3*LEFT)
		self.play(ShowCreation(r))
		self.wait()

		t1=TextMobject("3")
		t1.set_color(BLUE)
		t2=TextMobject("4")
		t2.set_color(BLUE)
		t1.next_to(r, LEFT)
		t2.next_to(r, DOWN)
		self.play(Write(t1))
		self.play(Write(t2))
		self.wait()

		qanak=TexMobject("\\text{Քանակ}","=")
		q=[]
		q.append(TexMobject(0))
		group=VGroup(qanak, q[0])
		group.arrange(RIGHT)
		group.shift(3*DOWN)
		self.play(ShowCreation(group))
		for i in range(1,5):
			for j in range(1,4):
				x=s.copy()
				self.play(ApplyMethod(x.shift, (4+i)*LEFT+(j-2)*UP, run_time=0.5))
				k=(i-1)*3+j
				t=TexMobject(k)
				t.shift(q[0].get_center())
				q.append(t)
				self.play(ReplacementTransform(q[k-1],q[k]), run_time=0.5)
		self.wait()

class tryagain(Scene):
	def construct(self):
		q=agh_array_2(1, 6, 5, BLUE, 0.5, 0.5)
		for i in range(6):
			for j in range(5):
				self.play(ShowCreation(q[i][j]))
		self.wait()