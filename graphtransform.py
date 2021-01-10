from manimlib.imports import *
import numpy as np

class cos(GraphScene):
	CONFIG = {
		"x_min" : -12,
		"x_max" : 12,
		"y_min" : -3,
		"y_max" : 3,
		"graph_origin": ORIGIN,
		"axes_color" : BLUE,
		"x_labeled_nums": range(-10, 12, 2),
	}
	def construct(self):
		def cos2(x):
			return np.cos(2*x)
		def cosq(x):
			return np.cos(x)**2
		self.setup_axes(animate=True)
		self.wait()
		cos=self.get_graph(np.cos, x_min=-10, x_max=10)
		self.play(Write(cos))
		cos2=self.get_graph(cos2,x_min=-10, x_max=10)
		self.play(ReplacementTransform(cos, cos2))
		self.wait()
		cosq=self.get_graph(cosq,x_min=-10, x_max=10)
		self.play(ReplacementTransform(cos2, cosq))
		self.wait()