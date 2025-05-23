from manim import * #Import everything from manim
class Example(Scene): #Kuch hai
    def construct(self):
        cube=Square(color=GREEN,fill_opacity=0.5)
        self.add(cube)