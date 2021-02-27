from manimlib.imports import *
from erkr import *
from Grid_Funtions import *
from Useful_Funtions import *

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

		self.play(Uncreate(n1))
		self.play(FadeIn(n1c))
		self.wait()
		self.play(Uncreate(n2))
		self.play(FadeIn(n2c))
		self.wait()
		self.play(Uncreate(n3))
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
		self.play(FadeOut(groupt),FadeOut(binom))
		self.wait()
		self.play(FadeOut(vern))
		self.wait()

class sequence(Scene):
	def construct(self):
		#vern=vernagir(TextMobject("Հաջորդականություններ"))
		#self.play(Write(vern))
		ast=TexMobject(
			"1",", ",
			"2",", ",
			"4",", ",
			"8",", ",
			"16",", ",
			"32",", ",
			"...")
		ast.shift(UP)
		ast_c=ast.copy()
		self.play(Write(ast))
		self.wait()

		dot=TexMobject("\\cdot")
		two=TexMobject("2")
		eq=TexMobject("=")

		for i in range(1,6):
			ast1=ast[2*i].copy()
			ast2=ast[2*(i-1)].copy()
			ast1.set_color(BLUE)
			ast2.set_color(RED)
			self.add(ast1,ast2)
			self.play(
				ApplyMethod(ast1.shift, DOWN-0.4*LEFT+(3-i)*1.2*LEFT),
				ApplyMethod(ast2.shift, DOWN+0.4*LEFT+(3-i)*1.2*LEFT)
				)
			t=two.copy()
			t.move_to(ast1.get_center()/2+ast2.get_center()/2)
			d=dot.copy()
			d.move_to(t.get_center()/2+ast2.get_center()/2)
			eq=eq.copy()
			eq.move_to(ast1.get_center()/2+t.get_center()/2)
			self.play(Write(d), Write(t), Write(eq))
		
		harc=TexMobject("?")
		harc.next_to(ast[11], RIGHT)
		
		self.play(ReplacementTransform(ast[12], harc))
		fib=TexMobject(
			"1",", ",
			"1",", ",
			"2",", ",
			"3",", ",
			"5",", ",
			"8",", ",
			"...")

		fib.shift(DOWN)
		self.play(Write(fib))
		self.wait()

class Sequence(Scene):
	def construct(self):
		ast=TexMobject(
			"1",", ",
			"2",", ",
			"4",", ",
			"8",", ",
			"16",", ",
			"32",", ",
			"?")
		ast.set_width(4)
		ast.to_edge(UP)
		ast_c=ast.copy()
		self.play(Write(ast))
		self.wait()

		for i in range(1,7):
			ast1=ast[2*i].copy()
			ast2=ast[2*(i-1)].copy()
			ast1.set_color(BLUE)
			ast2.set_color(RED)
			self.add(ast1,ast2)
			if(i!=6):
				hav=TexMobject(2**(i-1),"\\cdot",2,"=",2**i)
			else:
				hav=TexMobject(2**(i-1),"\\cdot",2,"="," ?")
			hav.set_width(2)
			hav[0].set_color(RED)
			hav[4].set_color(BLUE)
			if(i <= 3):
				hav.move_to(ast.get_center()+4*LEFT+i*DOWN)
			else:
				hav.move_to(ast.get_center()+4*RIGHT+(i-3)*DOWN)
			self.play(
				ReplacementTransform(ast1,hav[4]),
				ReplacementTransform(ast2,hav[0]),
				Write(hav[1]),
				Write(hav[2]),
				Write(hav[3])
				)
			self.wait()
			if(i==6):
				last=TexMobject("64")
				last.move_to(hav[4])
				last.set_width(hav[4].get_width())
				self.play(ReplacementTransform(hav[4],last))
				self.play(
					FadeOut(ast[12]),
					ApplyMethod(last.copy().move_to,ast[12]),
					#last.set_color(WHITE)
					)
				self.wait()

class Pascal(Scene):
	def construct(self):
		height=0.75
		width=0.4
		
		x=Pascal_Tr(height, width, 7)
		x_VG=matrix_to_VGroup(x)
		x_VG.shift(2.5*UP+3*LEFT)

		rects=srj_ugh(x)
		rects_VG=matrix_to_VGroup(rects)

		self.play(
			ShowCreation(rects_VG),
			*[Write(x[i][0]) for i in range(len(x))],
			*[Write(x[j][j]) for j in range(1,len(x))]
			)
		self.wait()

		for i in range(5):
			for j in range(1,i):
				nax1=x[i-1][j-1].copy()
				nax1.set_color(ORANGE)
				nax2=x[i-1][j].copy()
				nax2.set_color(ORANGE)
				self.add(nax1,nax2)

				question=TexMobject("?")
				question.move_to(x[i][j])
				question.set_color(GREEN)
				x[i][j].set_color(GREEN)
				self.play(Write(question))
				
				equation=TexMobject(ncr(i-1,j-1),"+",ncr(i-1,j),"=", ncr(i,j))
				equation.move_to(x[2][2].get_center()+3*RIGHT)
				equation[0].set_color(ORANGE)
				equation[2].set_color(ORANGE)
				
				self.play(
					ReplacementTransform(nax1,equation[0]),
					ReplacementTransform(nax2,equation[2]),
					Write(equation[1]),
					Write(equation[3])
					)
				equation[4].set_color(GREEN)
				self.play(Write(equation[4]))
				
				self.play(
					FadeOut(question),
					TransformFromCopy(equation[4],x[i][j])
					)
				x[i][j].set_color(WHITE)
				self.play(FadeOut(equation))
		
		self.play(
			*[FadeIn(x[5][i]) for i in range(1,5)],
			)
		self.wait()
		self.play(
			*[FadeIn(x[6][j]) for j in range(1,6)]
			)
		self.wait()

class Pascal_fib(GraphScene):
	def construct(self):
		height=0.75
		width=0.4
		
		x=Pascal_Tr(height, width, 7)
		x_VG=matrix_to_VGroup(x)
		x_VG.shift(2*UP+2*LEFT)

		x_c_VG=x_VG.copy()
		self.play(ShowCreation(x_c_VG),ShowCreation(x_VG))
		self.wait()

		lines=Pascal_Fib(x,2.2)
		self.play(
			*[ShowCreation(lines[i])
			 for i in range(7)]
			 )
		self.wait()

		coord2=x[0][0].get_center()+2.2*(height*UP+3*width*RIGHT)
		change=height*2/3*UP
		for i in range(len(x)):
			line=[]
			for k in range(i, -1, -1):
				if(k>=i-k):
					line.append([k,i-k])
			for number in line:
				x[number[0]][number[1]].set_color(BLUE)
			self.wait()
			self.play(
				*[ApplyMethod(
					x[number[0]][number[1]].move_to,
					coord2-(number[0]+number[1])*change+(number[1]+1)*0.5*RIGHT+0.2*LEFT)
				for number in line]
				)
		self.wait()

class rows(Scene):
	def construct(self):
		height=0.75
		width=0.4
		
		x=Pascal_Tr(height, width, 7)
		x_VG=matrix_to_VGroup(x)
		x_VG.shift(2.5 * UP + 3 * LEFT)

		lines=Pascal_ast(x,3)
		self.play(*[ShowCreation(line) for line in lines])

		self.play(Write(x_VG))
		self.wait()
