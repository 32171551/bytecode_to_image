import csv
import os

bytecode_dir = "../bytecode"
dst_dir = "../dec"

if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)

bytecode_file_list = os.listdir(bytecode_dir)

for bytecode_file in bytecode_file_list:
    print(bytecode_file)
    bytecode_file_path = os.path.join(bytecode_dir, bytecode_file)
    f = open(bytecode_file_path, 'r').read()
    print(len(f))
    tmp_list = []
    for idx in range(4, len(f)):
        number = f[idx-2:idx]
        n = '0x' + str(number)
        n = int(n , 16)
        tmp_list.append(n)
    dst_path = os.path.join(dst_dir, bytecode_file.split('.')[0]+'.csv')
    dst_f = open(dst_path, 'w', encoding='utf-8')
    writer = csv.writer(dst_f)
    writer.writerow(tmp_list)




