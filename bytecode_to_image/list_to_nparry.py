import os
import numpy as np
import cv2
import csv

path = "../dec"
new_path = "../sc_img"
if not os.path.exists(new_path):
    os.mkdir(new_path)

file_list = os.listdir(path)

for f_name in file_list:
    print(f_name)
    file_path = os.path.join(path, f_name)
    read_file = open(file_path, 'r', encoding='utf-8-sig') #리스트 형식임
    r = list(csv.reader(read_file))
    r_list = r[0]
    dst_name = f_name.split('.')[0] + '.jpg'
    dst_path = os.path.join(new_path, dst_name)

    file_size = os.path.getsize(file_path)
    width = 32
    if 10000 < file_size <= 30000:
        width = 64
    elif 30000 < file_size <= 60000:
        width = 128
    elif 60000 < file_size:
        width = 256

    # print(file_name)
    height = (len(r_list) // width) + 1
    array = np.zeros((height, width))
    # print(array.shape)

    for idx, number in enumerate(r_list):
        try:
            col = int(idx % width)  # 나머지
            row = int(idx // width)  # 정수 몫
            # print(number)
            array[row][col] = int(number) # /9.0
        except IndexError:
            col = int(idx % width)  # 나머지
            row = int(idx // height)  # 정수 몫
            print(idx, ' / ', row, ' / ',  col)

    cv2.imwrite(dst_path, array)
