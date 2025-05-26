from manim import * #Import everything from manim
import numpy as np
vel=0
class Blockonspring(ThreeDScene):#Kuch hai
    def construct(self):
        x0=0    #Equilibrium position of block(unstretched string)
        m=1     #mass of block
        k=5     #spring constant
        A=2     #Amplitude(initial displacement from equilibrium in this case as v_init=0)
        phi=0   #phase constant
        omega=(k/m)**0.5
        cube=Cube(color=DARK_BLUE,fill_opacity=0.5).move_to([-3,-2,0],aligned_edge=LEFT).scale(0.5) #initialize block
        wall=Surface(lambda u,v:[-6,u,v],u_range=[-2.5,2.5],v_range=[-5,5],checkerboard_colors=False,fill_color=GREEN,stroke_opacity=0,stroke_color=GREEN)
        floor=Surface(lambda u,v:[u,-2.5,v],u_range=[-6,4],v_range=[-5,5],checkerboard_colors=False,fill_color=GREEN,stroke_opacity=0,stroke_color=GREEN)
        t=ValueTracker(0)
        def move(mob,dt):
            global vel
            xfromq=mob.get_critical_point(LEFT)[0]-x0  #Extension or contraction of spring
            acc=-(omega**2)*xfromq
            vel+=acc*dt
            mob.shift(vel*dt*RIGHT)
        def zigzag(t):
            l=np.modf(31*(t/(cube.get_critical_point(LEFT)[0]+6)))[1]+1
            m=np.modf(31*(t/(cube.get_critical_point(LEFT)[0]+6)))[0]
            if l%2==0:
                return [t-6,0.7*m-2,0]
            else:
                return [t-6,0.7*(1-m)-2,0]
        def spiral(t):
            l=cube.get_critical_point(LEFT)[0]+6
            n=50
            r=0.5
            w=2*PI*r*n
            v=l
            return [v*t-6,r*np.sin(w*t)-2,r*np.cos(w*t)]
        spring=always_redraw(lambda : ParametricFunction(spiral,t_range=[0,1])) 
        self.add(wall)
        self.add(floor)
        self.add(spring)
        cube.add_updater(move)
        self.add(cube)
        self.wait()
        self.play(t.animate.set_value(15),run_time=15)
