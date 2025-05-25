from manim import *
import numpy as np

class NormalModeGraphs(Scene):
    def construct(self):
        # Time tracker
        t = ValueTracker(0)

        # Axis
        axis = NumberLine(x_range=[-3, 3], length=6, include_ticks=True)
        self.add(axis)

        # Mass points
        dot1 = Dot(color=BLUE).move_to([-2, 0, 0])
        dot2 = Dot(color=RED).move_to([2, 0, 0])
        self.add(dot1, dot2)

        # Parameters
        A = 1
        omega1 = 1
        omega2 = np.sqrt(3)

        # Labels
        label1 = Text("Mode 1: In-phase", font_size=36).to_edge(UP)
        label2 = Text("Mode 2: Out-of-phase", font_size=36).to_edge(UP)

        # === MODE 1 ===
        def update_mode1(mob, i):
            x = A * np.sin(omega1 * t.get_value())
            original_x = -2 if i == 0 else 2
            mob.move_to([original_x + x, 0, 0])

        dot1.add_updater(lambda m: update_mode1(m, 0))
        dot2.add_updater(lambda m: update_mode1(m, 1))

        self.play(Write(label1))
        self.play(t.animate.set_value(2 * np.pi), run_time=6, rate_func=linear)
        self.wait()
        self.remove(label1)
        dot1.clear_updaters()
        dot2.clear_updaters()

        # === MODE 2 ===
        t.set_value(0)
        dot1.add_updater(lambda m: dot1.move_to([-2 + A * np.sin(omega2 * t.get_value()), 0, 0]))
        dot2.add_updater(lambda m: dot2.move_to([2 - A * np.sin(omega2 * t.get_value()), 0, 0]))

        self.play(Write(label2))
        self.play(t.animate.set_value(2 * np.pi), run_time=6, rate_func=linear)
        self.wait()
#Animating n coupled oscillators and their normal modes
