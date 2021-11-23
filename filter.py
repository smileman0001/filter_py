from PIL import Image
import numpy as np


np.seterr(over='ignore')


def transform_to_mosaic(ix, iy, i_arr, i_size, i_step):
    """
    Данный метод заполняет массив(новую картинку) серым цветом с нужным оттенком
    :param ix: int
    :param iy: int
    :param i_arr
    :param i_size: int
    :param i_step: int
    """
    average_brightness = np.mean(i_arr[ix:ix + i_size, iy:iy + i_size][:])
    i_arr[ix:ix + i_size, iy:iy + i_size][:] = int(average_brightness // i_step) * i_step


open_name = input('Введите назвние изображения : ')
save_name = input('Введите назвние выходного изображения : ')


img = Image.open(open_name)
arr = np.array(img)

size = int(input('Введите длину боковой стороны мозайки (например: 10 (x*x)) : '))
gradation = int(input('Введите градацию серого (например: 5) : '))
step = 255 // gradation

width = len(arr)
height = len(arr[1])

for x in range(0, width - size + 1, size):
    for y in range(0, height - size + 1, size):
        transform_to_mosaic(x, y, arr, size, step)
res = Image.fromarray(arr)
res.save(save_name)
