from manimlib.imports import *
from erkr import *
from Grid_Funtions import *
import numpy as np

def vernagir(header):
	''''''
	lin=Line(5*LEFT, 5*RIGHT)
	vern=VGroup(header, lin)
	vern.arrange(DOWN)
	vern.to_edge(UP)
	return vern
def center(array):
	'''array-ի բոլոր տարրերի կենտրոնների ծանրության կենտրոնը
	type: coordinates'''
	mean=0
	for i in range(len(array)):
		mean+=array[i].get_center()
	mean/=len(array)
	return mean
def array_to_VGroup(array):
	'''array-ի բոլոր տարրերով VGroup'''
	x=array[0]
	for i in range(1,len(array)):
		x=VGroup(x,array[i])
	return x
def matrix_to_VGroup(matrix):
	'''matrix-ի բոլոր տարրերով VGroup'''
	x=matrix[0][0]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if(i!=0 or j!=0):
				x=VGroup(x, matrix[i][j])
	return x

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom
def Pasc_Tr(l):
	listok=[]
	for i in range(l):
		for j in range(i+1):
			listok.append(ncr(i,j))
	return listok
def Pascal_Tr(height, width, l):
	'''matrix, որը
	1․ Պասկալի եռանկյան առաջին l տողերն են, երբ l-ը թիվ է
	2․ Երբ l-ը list է'''
	listik=[]
	if(type(l)!=list):
		l=Pasc_Tr(l)
	cursor0=0
	cursor1=0
	count=0
	togh=0
	erk=len(l)
	while(count<erk):
		listuk=[]
		for i in range(min(erk-count, togh+1)):
			new=TexMobject(l[count])
			new.move_to(cursor0*RIGHT+cursor1*UP)
			listuk.append(new)
			count+=1
			cursor0+=2*width
		cursor1-=height
		cursor0-=((togh+1)*2+1)*width
		togh+=1
		listik.append(listuk)
	return listik
def srj_ugh(matrix):
	h=matrix[0][0].get_y()-matrix[1][0].get_y()
	w=matrix[0][0].get_x()-matrix[1][0].get_x()
	qar=[]
	for i in range(len(matrix)):
		q=[]
		for j in range(len(matrix[i])):
			rec=Rectangle(height=h, width=2*w)
			rec.move_to(matrix[i][j])
			q.append(rec)
		qar.append(q)
	return qar

def Pascal_Fib(matrix, mult):
	lines=[]
	h=matrix[0][0].get_y()-matrix[1][0].get_y()
	w=matrix[0][0].get_x()-matrix[1][0].get_x()
	coord1 = matrix[0][0].get_center()
	coord2 = matrix[0][0].get_center() + mult * (h * UP + 3 * w * RIGHT)
	togh = len(matrix)
	for i in range(togh):
#		line=Line(coord1-2/3*UP*i,coord2-2/3*UP*i)
		line=DashedLine(coord1+i*(h*DOWN+w*LEFT),coord2-h*2/3*UP*i)
		lines.append(line)
	return lines

def Pascal_ast(matrix, mult):
	lines=[]
	h=matrix[0][0].get_y()-matrix[1][0].get_y()
	w=matrix[0][0].get_x()-matrix[1][0].get_x()

	coord1=matrix[0][0].get_center()
	coord2=matrix[0][0].get_center()+mult*(3*w*RIGHT)

	togh=len(matrix)
	for i in range(togh):
		line=DashedLine(coord1+i*(h*DOWN+w*LEFT),coord2-h*i*UP)
		lines.append(line)
	return lines
