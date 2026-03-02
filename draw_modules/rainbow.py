
import simple_draw as sd

def draw_rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    point = sd.get_point(450, -50)
    radius = 800
    step = 10
    color_index = 0
    for _ in range(7):
        radius += step
        color = rainbow_colors[color_index]
        sd.circle(center_position=point, radius=radius, color=color, width=step)
        color_index += 1
