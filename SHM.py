from manim import *
import numpy as np

class BlockOnSpring(Scene):
    def construct(self):
        # System parameters
        m = 1
        k = 5
        A = 2
        omega = np.sqrt(k / m)
        wall_x = -4
        wall_thickness = 0.3
        wall_front = wall_x + wall_thickness

        # Wall
        wall = Rectangle(width=wall_thickness, height=3, color=GREY, fill_opacity=1)
        wall.move_to([wall_front - wall_thickness / 2, 0, 0])
        self.add(wall)

        # Surface
        surface_y = -1.5
        surface = Line(start=[-6, surface_y, 0], end=[6, surface_y, 0], color=WHITE)
        self.add(surface)

        # Block
        block = Square(color=BLUE_D, fill_opacity=0.7).scale(0.7)
        block_half = block.width / 2
        block_y = surface_y + block.height / 2  # Bottom touches surface
        initial_x = wall_front + A
        block.move_to([initial_x, block_y, 0])

        # Time Tracker
        t = ValueTracker(0)

        # SHM physical x-position
        def get_physical_x():
            return wall_front + A * np.cos(omega * t.get_value())

        # Spring (realistic curve)
        def get_spring():
            spring_start = np.array([wall_front, block_y, 0])
            x_phys = get_physical_x()
            x_vis = max(x_phys, wall_front + block_half)
            spring_end = [x_vis - block_half, block_y, 0]
            return self.create_spring(spring_start, spring_end, coils=15, radius=0.15)

        spring = always_redraw(get_spring)

        # Block updater
        def update_block(mob):
            x_phys = get_physical_x()
            x_vis = max(x_phys, wall_front + block_half)
            mob.move_to([x_vis, block_y, 0])

        block.add_updater(update_block)

        # Add and play
        self.add(block, spring)
        self.play(t.animate.set_value(15), run_time=15, rate_func=linear)

    # Realistic spring using sine wave-like curve
    def create_spring(self, start, end, coils=15, radius=0.15):
        start = np.array(start)
        end = np.array(end)
        vector = end - start
        length = np.linalg.norm(vector)
        if length == 0:
            return VMobject()

        direction = vector / length
        perpendicular = np.array([-direction[1], direction[0], 0])

        points = []
        num_points = coils * 20  # More points = smoother spring
        for i in range(num_points + 1):
            alpha = i / num_points
            base_point = start + alpha * vector
            sine_offset = radius * np.sin(2 * np.pi * coils * alpha)
            point = base_point + sine_offset * perpendicular
            points.append(point)

        return VMobject().set_points_as_corners(points).set_stroke(RED, width=3)
