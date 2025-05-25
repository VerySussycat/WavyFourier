from manim import *
import numpy as np

class GeneralNormalModes(Scene):
    def construct(self):
        N = 5  # Number of oscillators
        A = 1  # Amplitude
        spacing = 1.5  # Distance between oscillators
        omega_base = 1  # Base frequency
        t = ValueTracker(0)

        # Initialize mode counter
        self.current_mode = 0

        # Create oscillator dots
        dots = VGroup()
        for i in range(N):
            dot = Dot().move_to([spacing * (i - (N - 1) / 2), 0, 0])
            dots.add(dot)
        self.add(dots)

        # Axes line
        axis = NumberLine(x_range=[-N, N], length=spacing * (N + 1), include_ticks=False).move_to([0, 0, 0])
        self.add(axis)

        # Label for mode
        label = always_redraw(lambda: Text(f"Mode {self.current_mode + 1}", font_size=36).to_edge(UP))
        self.add(label)

        # Show normal modes
        for mode in range(N):
            self.current_mode = mode
            omega_n = 2 * omega_base * np.sin((mode + 1) * np.pi / (2 * (N + 1)))

            # Add updaters to each dot
            for i, dot in enumerate(dots):
                def make_updater(i=i, mode=mode, omega_n=omega_n):
                    def updater(mob):
                        x = spacing * (i - (N - 1) / 2)
                        displacement = A * np.sin((i + 1) * (mode + 1) * np.pi / (N + 1)) * np.sin(omega_n * t.get_value())
                        mob.move_to([x, displacement, 0])
                    return updater
                dot.add_updater(make_updater())

            self.play(t.animate.set_value(2 * np.pi), run_time=5, rate_func=linear)
            self.wait(0.5)
            t.set_value(0)

            # Remove updaters
            for dot in dots:
                dot.clear_updaters()
