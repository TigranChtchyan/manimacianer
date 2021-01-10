from manimlib.imports import *
import numpy as np

class dch(Scene):
	def construct(self):
		dch1.construct(self)
		dch1.remove(self)
		dch2.construct(self)
		dch3.construct(self)
		dch4.construct(self)
class dch1(Scene):
	def construct(self):
		header1=TextMobject(
			"Քառակուսի հավասարման լուծումը հեշտացնելու համար կա մի հնարք:",
		)
		header2=TexMobject(
			"\\text{Այն կիրառվում է, երբ } ax^2+bx+c=0 \\text{ hավասարման } b \\text{ գործակիցը զույգ է:}",
			tex_to_color_map={"b" : BLUE}
		)
		header3=TexMobject(
			"\\text{Այսինքն, կարող ենք գրել } b = 2k \\text{:}",
			tex_to_color_map={"b" : BLUE, "2k" : RED}
		)
		group=VGroup(header1,header2,header3)
		group.arrange(DOWN)
		group.set_width(12)
		group.to_edge(UP)
		self.play(Write(group), run_time=3)
		self.wait(2)

class dch2(Scene):
	def construct(self):
		t0=TextMobject(
			"Լուծման դասական եղանակ",
		)
		t1=TexMobject(
			"ax^2+bx+c=0",
			tex_to_color_map={"b" : BLUE}
		)
		t2=TexMobject(
			"D=b^2-4ac",
			tex_to_color_map={"b" : BLUE}
		)
		t3=TexMobject(
			"x_{1,2}=\\frac{-b \\pm \\sqrt{D}}{2a}",
#			tex_to_color_map={"-b" : BLUE}
		)
		group=VGroup(t0,t1,t2,t3)
		group.arrange(DOWN)
		self.play(Write(group), run_time=3)
		self.wait()
		self.play(ApplyMethod(group.shift, 4*RIGHT))

class dch3(Scene):
	def construct(self):
		t0=TextMobject(
			"Լուծման այլ եղանակ",
		)
		t1=TexMobject(
			"ax^2+2kx+c=0",
			tex_to_color_map={"k" : RED}
		)
		t2=TexMobject(
			"D=(2k)^2 - 4ac",
			tex_to_color_map={"k" : RED}
		)
		t3=TexMobject(
			"x_{1,2}=\\frac{-2 k \\pm \\sqrt{D} }{2a}",
#		tex_to_color_map={"2k" : RED}
		)
		group=VGroup(t0,t1,t2,t3)
		group.arrange(DOWN)
		group.to_edge(RIGHT)
		group.move_to(4*LEFT)
		self.play(Write(group), run_time=3)

		t2n=TexMobject(
			"D=4k^2 - 4ac",
			tex_to_color_map={"k" : RED}
		)
		t2n.move_to(t2)
		self.play(ReplacementTransform(t2,t2n))
		self.wait()
		t2nn=TexMobject(
			"D=4(k^2 - ac)",
			tex_to_color_map={"k" : RED}
		)
		t2nn.move_to(t2)
		self.play(ReplacementTransform(t2n,t2nn))
		self.wait()
		t3n=TexMobject(
			"x_{1,2}=\\frac{-2 k \\pm \\sqrt{4(k^2 - ac)} }{2a}",
#		tex_to_color_map={"2k" : RED}
		)
		t3n.move_to(t3)
		self.play(ReplacementTransform(t3,t3n))
		self.wait()
		t3nn=TexMobject(
			"x_{1,2}=\\frac{-2 k \\pm 2\\sqrt{k^2 - ac} }{2a}",
#		tex_to_color_map={"2k" : RED}
		)
		t3nn.move_to(t3)
		self.play(ReplacementTransform(t3n,t3nn))
		self.wait()
		t3nnn=TexMobject(
			"x_{1,2}=\\frac{-k \\pm \\sqrt{k^2 - ac} }{a}",
#		tex_to_color_map={"2k" : RED}
		)
		t3nnn.move_to(t3)
		self.play(ReplacementTransform(t3nn,t3nnn))
		self.wait()
		t2nnn=TexMobject(
			"D_{1}=\\frac{D}{4}=k^2 - ac",
			tex_to_color_map={"k" : RED}
		)
		t2nnn.move_to(t2)
		self.play(ReplacementTransform(t2nn,t2nnn))
		self.wait()

class dch4(Scene):
	def construct(self):
		t1=TextMobject("Այսպիսով՝ ձևափոխությունների շնորհիվ ստացանք ավելի պարզ բանաձև")
		t2=TexMobject("\\text{Այժմ } D \\text{-ի փոխարեն կարող ենք հաշվել } \\frac{D}{4} \\text{-ը}")
		group=VGroup(t1,t2)
		group.arrange(DOWN)
		group.to_edge(DOWN)
		group.set_width(12)
		self.play(Write(group), run_time=3)
