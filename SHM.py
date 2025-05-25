from manim import * #Import everything from manim
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
        cube=Square(color=DARK_BLUE,fill_opacity=0.5).move_to([-3,-2,0],aligned_edge=LEFT).scale(0.5) #initialize block
        wall=Line([-6,-2.5,0],[-6,4,0])
        floor=Line([-6,-2.5,0],[6,-2.5,0])
        t=ValueTracker(0)
        def move(mob,dt):
            global vel
            xfromq=mob.get_critical_point(LEFT)[0]-x0  #Extension or contraction of spring
            acc=-(omega**2)*xfromq
            vel+=acc*dt
            mob.shift(vel*dt*RIGHT)
        def zigzag(t):
            l=np.modf(30*(t/(cube.get_critical_point(LEFT)[0]+6)))[1]+1
            m=np.modf(30*(t/(cube.get_critical_point(LEFT)[0]+6)))[0]
            if l%2==0:
                return [t-6,0.4*m-2.5,0]
            else:
                return [t-6,0.4*(1-m)-2.5,0]
        spring=always_redraw(lambda : ParametricFunction(zigzag,t_range=[0,cube.get_critical_point(LEFT)[0]+6])) 
        self.add(wall)
        self.add(floor)
        self.add(spring)
        cube.add_updater(move)
        self.add(cube)
        self.wait()
        self.play(t.animate.set_value(15),run_time=15)
        
            



        
        
