# Вариант 0

import struct as st
from math import sin, cos, pi


def set_bmp_header(width, height):
    filetype = 19778  # 4D 42 - BM 16 384 + 3 328+ 64 + 2 4*16**3+13*16**2+4*16+2
    reserved_1 = 0
    reserved_2 = 0
    pixel_offset = 62
    file_size = width * height + pixel_offset
    return st.pack('<HL2HL', filetype, file_size, reserved_1, reserved_2, pixel_offset)


def set_info_header(width, height):
    header_size = 40
    image_width = width
    image_height = height
    planes = 1
    bits_per_pixel = 8
    compression = 0
    image_size = 0
    x_pixel_per_meter = 0
    y_pixel_per_meter = 0
    amount_colors = 2
    important_colors = 0
    return st.pack('<3L2H6L', header_size, image_width, image_height, planes, bits_per_pixel, compression,
                   image_size, x_pixel_per_meter, y_pixel_per_meter, amount_colors, important_colors)


def set_color():
    blue = (255, 0, 0, 255)
    white = (255, 255, 255, 0)
    return st.pack('<8B', *blue, *white)


width = 500
height = 500
function_pixels = []
t = 0
step = 0.005
x_minimum = float('inf')
y_minimum = float('inf')

while t <= pi * 10:
    x = round((cos(t)+cos(6.2*t)/6.2), 2)
    if x < x_minimum:
        x_minimum = x
    y = round((sin(t)-sin(6.2*t)/6.2), 2)
    if y < y_minimum:
        y_minimum = y
    function_pixels.append((x, y))
    t += step

with open('result.BMP', 'wb') as file:
    file.write(set_bmp_header(width, height))
    file.write(set_info_header(width, height))
    file.write(set_color())
    y_of_pixel = y_minimum
    for i in range(height):
        x_of_pixel = x_minimum
        for j in range(width):
            if (x_of_pixel, y_of_pixel) in function_pixels:
                file.write(st.pack('<B', 0))
            else:
                file.write(st.pack('<B', 1))
            x_of_pixel = round(x_of_pixel + step, 3)
        y_of_pixel = round(y_of_pixel + step, 3)
