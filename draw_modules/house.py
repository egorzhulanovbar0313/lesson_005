import simple_draw as sd

def draw_house():
    x_start = 300
    y_start = 0
    brick_width = 40
    brick_height = 20
    rows = 15
    cols = 10

    for row in range(rows):
        x_offset = 0 
        if row % 2 == 1:
            x_offset = brick_width // 2

        for col in range(cols):
            x = x_start + x_offset + col * brick_width
            y = y_start + row * brick_height
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x + brick_width, y + brick_height)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1, color=sd.COLOR_ORANGE)
    sd.rectangle(left_bottom=sd.get_point(x_start, y_start), right_top=sd.get_point(x + brick_width + 20, y + brick_height), color=sd.COLOR_ORANGE, width=1)