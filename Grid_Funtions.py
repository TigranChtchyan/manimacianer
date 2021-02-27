from manimlib.imports import *
from Useful_Funtions import *
from erkr import *
import numpy as np

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
def qarakusikner_2(width,n,color,midtogh):
	t=qar_array_2(width,n,color,midtogh)
	x=t[0]
	for i in range(1,len(t)):
		x=VGroup(x,t[i])
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

def aghyusak(width, togh, syun, color):
	t=qarakusikner(width, syun, color)
	a=t
	for i in range(1,togh):
		s=a.copy()
		s.shift((i*width)*UP)
		t=VGroup(t, s)
	t.shift((togh-1)*width*0.5*DOWN)
	return t
def aghyusak_2(width, togh, syun, color, midtogh, midsyun):
	k=agh_array_2(width, togh, syun, color, midtogh, midsyun)
	x=k[0][0]
	for i in range(len(k)):
		for j in range(len(k[0])):
			if(i!=0 or j!=0):
				x=VGroup(x,k[i][j])
	return x

	k=[]
	for i in range(togh):
		s=qar_array_2(width, syun, color, midtogh)
		for j in range(syun):
			s[j].shift((i*(width+midsyun)*UP))
			s[j].shift((togh-1)*(width+midsyun)*0.5*DOWN)
		k.append(s)
	return 

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
