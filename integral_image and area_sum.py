from typing import Tuple, TypeVar
import numpy as np

Integral_Image = TypeVar("Integral_Image", np.array, int)

a = np.random.randint(0,15,(1024,1024))

def integral_image(image: np.array) -> Integral_Image:
    column_sums = np.add.accumulate(image)
    integral_image_total = np.add.accumulate(column_sums, 1)
    return integral_image_total

def area_sum_finder(integral_image: Integral_Image, top_left_bound: Tuple[int, int], bottom_right_bound: Tuple[int, int]) -> int:
    top_left_y, top_left_x = top_left_bound
    bottom_right_y, bottom_right_x = bottom_right_bound

    top_left_outer_bound =  integral_image[top_left_y - 1, top_left_x - 1]
    top_right_outer_bound = integral_image[top_left_y - 1, bottom_right_x]
    bottom_left_outer_bound = integral_image[bottom_right_y, top_left_x - 1]
    bottom_right_inner_bound = integral_image[bottom_right_bound]

    area_sum = bottom_right_inner_bound + top_left_outer_bound - (top_right_outer_bound + bottom_left_outer_bound)
    return area_sum


i_image = integral_image(a)
area_sum = area_sum_finder(i_image, (125,29), (1022,900))
print(area_sum)
print(a)


