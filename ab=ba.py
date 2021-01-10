from manimlib.imports import  *
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


def center(arr):
	mean=0
	for i in range(len(arr)):
		mean+=arr[i].get_center()
	mean/=len(arr)
	return mean
def arr_VGroup(arr):
	x=arr[0]
	for i in range(1,len(arr)):
		x=VGroup(x,arr[i])
	return x
def matrix_VGroup(matrix):
	x=matrix[0][0]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if(i!=0 or j!=0):
				x=VGroup(x, matrix[i][j])
	return x
class abba(Scene):
	def construct(self):
		agh1=aghyusak_2(0.75,4,6,BLUE,0, 0.4)
		ax1=agh_array_2(0.75,4,6,BLUE,0, 0.4)
		agh2=agh1.copy()
		ax2=ax1.copy()
		agh1.shift(3.5*LEFT)
		ax1.shift(3.5*LEFT)
		agh2.rotate(PI/2)
		agh2.shift(4*RIGHT)

		group=matrix_VGroup(ax1)

		tiv1=TexMobject("4")
		tiv2=TexMobject("6")
		tiv1.next_to(agh1, LEFT)
		tiv2.next_to(agh1, UP)

		self.play(ShowCreation(agh1))
		self.play(Write(tiv1), Write(tiv2))
		self.wait()

		agh1c=agh1.copy()
		tiv1c=tiv1.copy()
		tiv2c=tiv2.copy()

		num1=TexMobject("4")
		num1.next_to(agh2, UP)
		num2=TexMobject("6")
		num2.next_to(agh2, LEFT)
		
		self.play(
			ReplacementTransform(agh1c, agh2),
			ReplacementTransform(tiv1c, num1),
			ReplacementTransform(tiv2c, num2),
		)

		self.wait()
		x=TexMobject(
			"4","\\cdot","6", 
			"=",
			"6","\\cdot", "4"
		)
		x.shift(3*DOWN)
		self.play(
			ReplacementTransform(tiv1.copy(), x[0]),
			Write(x[1]),
			ReplacementTransform(tiv2.copy(), x[2])
		)
		self.wait()
		self.play(Write(x[3]))
		self.wait()
		self.play(
			ReplacementTransform(num2.copy(), x[4]),
			Write(x[5]),
			ReplacementTransform(num1.copy(), x[6])
		)
		self.wait()