import simple_draw as sd

def draw_tree():
    def branches(start_point, angle, length, delta, color):
        if length < 10:
            return
        elif 10 < length < 20:
            color = sd.COLOR_GREEN
        vector = sd.get_vector(start_point=start_point, angle=angle, length=length)
        vector.draw(color=color, width=2)
        next_point = vector.end_point
        next_length = length * 0.75
        branches(start_point=next_point, angle=angle - delta, length=next_length, delta=delta, color=color)
        branches(start_point=next_point, angle=angle + delta, length=next_length, delta=delta, color=color)

    branches(start_point=sd.get_point(950, 0), angle=90, length=100, delta = 30, color=sd.COLOR_DARK_ORANGE)