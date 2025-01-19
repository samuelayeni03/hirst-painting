
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for i in range(30):
    rgb = colors[i].rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    color_tuple = (red, green, blue)
    rgb_colors.append(color_tuple)

print(rgb_colors)