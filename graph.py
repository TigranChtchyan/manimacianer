from manimlib.imports import *
import numpy as np
class funkcia(GraphScene):
	CONFIG={
	"y_max" : 10,
	"y_min" : 0,
	"x_max" : 10,
	"x_min" : -10,
	"y_tick_frequency" : 2,
	"x_tick_frequency" : 2,
	"x_axis_width": 6,
	"y_axis_height": 3,
	"axes_color" : ORANGE,
	}
	def construct(self):
		self.graph_origin = -0.5 * DOWN#3 * LEFT
		self.setup_axes(animate=True)
		self.wait()
		graph1=self.get_graph(lambda x: np.sin(x), color = BLUE, x_min=-9, x_max=9)
		self.graph_origin = 3*DOWN
		self.setup_axes(animate=True)
		self.wait()
		graph2=self.get_graph(lambda x: np.cos(x), color= BLUE, x_min=-9, x_max=9)
		group=VGroup(graph1,graph2)
		self.play(
			ShowCreation(group),
			run_time = 2
		)
		tex=TexMobject(
			"Ֆունկցիա",
		)
	#	tex.next_to()
		self.play(Write(tex))
		self.wait()
