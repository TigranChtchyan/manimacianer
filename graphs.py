from manimlib.imports import *
import numpy as np

class gr(GraphScene):
	CONFIG = {
		"x_min": -4,
        "x_max": 4,
        "x_axis_width": 9,
        "x_tick_frequency": 1,

        "x_leftmost_tick": None,  # Change if different from x_min
        
        "x_labeled_nums": None,
        "x_axis_label": "$f(x)$",
        "y_min": -32,
        "y_max": 32,
        "y_axis_height": 9,
        "y_tick_frequency": 10,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$f(x)^3+f(x)=x$",
        "axes_color": BLUE,
        "graph_origin": 1*DOWN,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
	}
	def construct(self):
		self.setup_axes(animate=True)
		
		t1=TexMobject(
			"\\text{Դիցուք ցանկացած իրական } x \\text{-ի համար } f(x) \\text{-ն այնպիսի իրական թիվ է, որ } f(x)^{3}+f(x)=x",
			tex_to_color_map={"f(x)^{3}+f(x)=x": GREEN}
		)
		t2=TexMobject("\\text{Հաշվել․} \\int_{0}^{2} f(x)dx")
		group=VGroup(t1,t2)
		group.set_width(12)
		group.arrange(DOWN)
		group.to_edge(UP)
		t2.shift(4*LEFT)
		self.play(Write(group))
		self.wait()

		graph=self.get_graph(lambda x: x**3+x, x_min=-3, x_max=3)
		self.play(ShowCreation(graph))
		self.wait()
		
		u=self.get_vertical_line_to_graph(2, graph)
		self.play(ShowCreation(u))
		self.wait()

		graph1=self.get_graph(lambda x: 10, x_min=0, x_max=2)
		self.play(ShowCreation(graph1))
		self.wait()

		mak=self.get_area(graph1, t_min=0, t_max=2)
		self.play(ShowCreation(mak))
		self.wait()

		x=self.get_area(graph, t_min=0, t_max=2)
		self.play(ShowCreation(x))
		self.wait()

		ben=TextMobject("LOX")
		self.play(GrowFromCenter(ben))
		self.wait()