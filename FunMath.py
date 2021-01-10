from manimlib.imports import *
import numpy as np

def vernagir(header):
	lin=Line(5*LEFT, 5*RIGHT)
	vern=VGroup(header, lin)
	vern.arrange(DOWN)
	vern.to_edge(UP)
	return vern

er=0

class overall(Scene):
	def construct(self):
		binom.construct(self)
		sequence.construct(self)

class binom(Scene):
	def construct(self):
		vern=vernagir(TexMobject("(a+b)^n"))
		self.play(ShowCreation(vern))
		self.wait()

		n0=TexMobject(
			"(","a","+","b",")^0=",
			"1",
			tex_to_color_map={"a" : BLUE, "b": YELLOW}
		)
		n1=TexMobject(
			"(","a","+","b",")^1=",
			"a", "+", "b",
			tex_to_color_map={"a" : BLUE, "b": YELLOW}
		)
		n2=TexMobject(
			"(","a","+","b",")^2=",
			"a", "^2", "+", "2", "a", "b", "+", "b", "^2",
			tex_to_color_map={"a" : BLUE, "b": YELLOW}
		)
		n3=TexMobject(
			"(","a","+","b",")^3=",
			"a","^3","+","3","a","^2","b","+","3","a","b","^2+","b^3",
			tex_to_color_map={"a" : BLUE, "b": YELLOW}
		)
	
		groupn=VGroup(n0,n1,n2,n3)
		groupn.arrange(DOWN)

		t0=TexMobject("n=0")
		t1=TexMobject("n=1")
		t2=TexMobject("n=2")
		t3=TexMobject("n=3")

		groupt=VGroup(t0,t1,t2,t3)
		groupt.arrange(DOWN)

		t1.move_to(n1.get_center()+6*LEFT)
		t0.move_to(n0.get_center()+6*LEFT)
		t3.move_to(n3.get_center()+6*LEFT)
		t2.move_to(n2.get_center()+6*LEFT)

		self.play(Write(n2))
		self.wait()
		self.play(Write(n3))
		self.wait()

		self.play(Write(t2))
		self.wait()
		self.play(Write(t3))
		self.wait()
		self.play(Write(t1))
		self.wait()
		self.play(Write(t0))
		self.wait()

		self.play(Write(n1))
		self.wait()
		self.play(Write(n0))
		self.wait()

		n0[5].set_color(RED)
		self.wait()

		n1c=TexMobject(
			"(","a","+","b",")^1=",
			"1","a", "+", "1" ,"b",
			tex_to_color_map={"a" : BLUE, "b": YELLOW}
		)
		n1c.move_to(n1.copy())
		n1c[5].set_color(RED)
		n1c[8].set_color(RED)

		n2c=TexMobject(
			"(","a","+","b",")^2=",
			"1","a", "^2", "+", "2", "a", "b", "+", "1","b", "^2",
			 tex_to_color_map={"a" : BLUE, "b": YELLOW}
		)
		n2c.move_to(n2.copy())
		n2c[5].set_color(RED)
		n2c[9].set_color(RED)
		n2c[13].set_color(RED)

		n3c=TexMobject(
			"(","a","+","b",")^3=",
			"1" ,"a","^3","+","3","a","^2","b","+","3","a","b","^2+", "1","b^3",
			tex_to_color_map={"a" : BLUE, "b": YELLOW}
		)
		n3c.move_to(n3.copy())
		n3c[5].set_color(RED)
		n3c[9].set_color(RED)
		n3c[14].set_color(RED)
		n3c[18].set_color(RED)

		self.play(FadeOut(n1))
		self.play(FadeIn(n1c))
		self.wait()
		self.play(FadeOut(n2))
		self.play(FadeIn(n2c))
		self.wait()
		self.play(FadeOut(n3))
		self.play(FadeIn(n3c))
		self.wait()

		c00=n0[5].copy()
		
		c10=n1c[5].copy()
		c11=n1c[8].copy()

		c20=n2c[5].copy()
		c21=n2c[9].copy()
		c22=n2c[13].copy()

		c30=n3c[5].copy()
		c31=n3c[9].copy()
		c32=n3c[14].copy()
		c33=n3c[18].copy()

		binom=VGroup(n0,n1c,n2c,n3c)
		er=VGroup(c00,c10,c11,c20,c21,c22,c30,c31,c32,c33)
		self.play(Write(er))
		self.play(FadeOut(groupt))
		self.play(FadeOut(binom))
		self.wait()
		self.play(FadeOut(vern))
		self.wait()
#		lin1=Line(n2c[5].get_center(),n1c[8].get_center())
#		self.play(ShowCreation(lin1))
#		self.wait()
class sequence(Scene):
	def construct(self):
		vern=vernagir(TextMobject("Հաջորդականություններ"))
		self.play(Write(vern))
		self.play(Write(er))