from manim import * #Import everything from 
import numpy as np
vel=0
class Blockonspring(Scene):#Kuch hai
    def construct(self):
        x0=0    #Equilibrium position of block(unstretched string)
        m=1     #mass of block
        k=5     #spring constant
        A=2     #Amplitude(initial displacement from equilibrium in this case as v_init=0)
        phi=0   #phase constant
        omega=(k/m)**0.5
        cube=Square(color=DARK_BLUE,fill_opacity=0.5).move_to([1,2,0],aligned_edge=LEFT)   #initialize block
        t=ValueTracker(0)
        def move(mob,dt):
            global vel
            xfromq=mob.get_critical_point(LEFT)[0]-x0  #Extension or contraction of spring
            acc=-(omega**2)*xfromq
            vel+=acc*dt
            mob.shift(vel*dt*RIGHT)
        cube.add_updater(move)
        self.add(cube)
        self.wait()
        self.play(t.animate.set_value(15),run_time=15)
        
            



        
        
