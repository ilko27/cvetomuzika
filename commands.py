named_colors = {
    "pink": [1.0, 0.01, 0.07],  # ff0311
    "cherry": [1.0, 0.059, 0.09], # ff0f17
    "turq": [0.1, 1, 0.1],
    "orange": [1.0, 0.07, 0.0],
    "sun": [1.0, 0.13, 0.0],
    "r": [1.0, 0.0, 0.0],
    "g": [0.0, 1.0, 0.0],
    "b": [0.0, 0.0, 1.0],
}


def new_colors():
    colors = input()
    if colors in named_colors:
        return named_colors[colors]
    if not (len(colors) == 6 or len(colors) == 7):
        return [1, 1, 1]
    if len(colors) == 7:
        colors = colors[1:]
    red = colors[:2]
    green = colors[2:4]
    blue = colors[4:6]

    new = [1, 1, 1]

    try:

        new[0] = int(red, base=16)
        new[1] = int(green, base=16)
        new[2] = int(blue, base=16)
    except:
        new = [1, 1, 1]

    for _, c in enumerate(new):
        new[_] = round(c/255, 3)
    print(new)

    return new
