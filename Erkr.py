# Այստեղ կան երկրաչափական ֆունկցիաներ

from manimlib.imports import *
import numpy as np

# Այս ֆունկցիան Circle շրջանագծի վրա առանձնացնում է այն կետը,
# որը կենտրոնի նկատմամբ phi անկյան տակ է 
def CirclePoint(Circle, phi):
	width=Circle.get_width()
	dot=Dot(Circle.get_center()+width/2*np.sin(phi)*UP+width/2*np.cos(phi)*RIGHT)
	return dot

#A և B կետերի միջնակետը
def segment_M(A,B):
	dot=Dot((A.get_center()+B.get_center())/2)
	return dot

# Շրջանագծի կենտրոնը
def kentron(Circle):
	dot=Dot(Circle.get_center())
	return dot

# Ուշադրություն, հաջորդող ֆունկցիաները կիսատ են

#A և B կետերի հեռավորությունը
def distance(A,B):
	x1=A.get_x()
	x2=B.get_x()
	y1=A.get_y()
	y2=A.get_y()
	distance=(x2-x1)**2+(y2-y1)**2
	distance=distance**0.5
	return distance

# Circle շրջանագծի վրա AB փոքր աղեղի միջնակետը (տրամագծի դեպքը խորհուրդ չի տրվում)
def arc_M(Circle, A,B):
	x0=Circle.get_x()
	y0=Circle.get_y()
	
	T=segment_M(A,B)
	x1=T.get_x()
	y1=T.get_y()

	r=Circle.get_width()/2
#	d=distance(kentron(Circle), T)

	coordx=(x1-x0)*r/d
	coordy=(y1-y0)*r/d
	dot=Dot(Circle.get_center()+coordx*RIGHT+coordy*UP)
	return dot

# ABC անկյունը նշող աղեղ, որը շառավիղը radius է
def angle(A, B, C, radius):
	c=Line(A,B)
	a=Line(B,C)
	arc=Arc()
	arc.set_width=2*radius
	return arc

# A կետից BC ուղղին տարված ուղղահայացի հիմքը
def ughhimq(A,B,C):
	return A
