import colorgram

colorsOfImage = colorgram.extract("E:\\Desktop\\Screens\\Physics\\last.jpg", 6)
colors = []

for color in colorsOfImage:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    col = (r, g, b)
    colors.append(col)

print(colors)
