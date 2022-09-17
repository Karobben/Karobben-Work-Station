#!/usr/bin/env python3.7

'''
This script is origin from tshirtman, https://gist.github.com/tshirtman/5466755,
If there has any offensive, please contack me and I will deleted it.
'''
from kivy.app import App
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation
from itertools import chain
from itertools import zip_longest as izip

kv = '''
#:import sin math.sin
#:import izip itertools.zip_longest
#:import chain itertools.chain
MyWidget:
    points:
        [
        (
        self.x + (x + 1) * self.width / (self.nb_points + 2),
        self.center_y + self.height * sin(x * self.mult * 1.0 / self.nb_points + self.offset) / 2
        )
        for x in range(self.nb_points)
        ]
    canvas:
        Color:
            rgba: self.color
        Line:
            points: self.points and list(chain(*self.points)) or []
            width: 0.1
        Line:
            points: self.points and list(chain(* ((x, self.top - y) for (x, y) in self.points))) or []
            width: 0.1
'''


class MyWidget(Widget):
    nb_points = NumericProperty(25)
    offset = NumericProperty(0)
    mult = NumericProperty(50)
    color = ListProperty([1, 0, 1, 1])


class MyApp(App):
    def build(self):
        self.root = Builder.load_string(kv)
        program = (
                Animation(mult=100, offset=10, d=10, t='in_out_back') +
                Animation(mult=10, offset=0, d=10, t='in_out_quad')
                )
        program &= (
                Animation(color=[0, 1, 1, 1], d=6) +
                Animation(color=[1, 1, 0, 1], d=6) +
                Animation(color=[1, 0, 1, 1], d=6)
                )

        program.start(self.root)
        program.bind(on_complete=lambda *args: program.start(self.root))
        return self.root


MyApp().run()
