import sys, shutil
from tqdm import tqdm, trange
import codecs
import os
import glob
from pathlib import Path
# def get_label_map(label_path):
#     label_map = dict()
#     with codecs.open(label_path, "r", encoding="utf-8") as f:
#         for line in f:
#             if not line:
#                 break
#             tokens = line.strip().split(",")
#             label_map[int(tokens[0])] = int(tokens[1])
#     return label_map

if __name__ == '__main__':
    crop_dir = '/data/disk3/cv2022/pollux/data/11_HPC-US-Sku/jam_exp_tide_0215/crops/'
    metadata_dir = 'datasets/tide27'

    SKUID = [1069705, 1069706, 1069709, 1069787, 1069812, 1069856, 1069933, 1069961, 1070017, 1070079, 
    1072412, 1090300, 1090392, 1107473, 1107474, 1107476, 1107477, 1107478, 1107480, 1107487, 1107572, 
    1107605, 1114091, 1114218, 1123596, 1127146, 1147667]
    label_map = dict()
    for i in range(len(SKUID)):
        label_map[SKUID[i]] = i

    dataset_dir = Path(metadata_dir)
    train_txt_file = dataset_dir / 'train.txt'
    val_txt_file = dataset_dir / 'val.txt'
    train_anno = []
    val_anno = []

    train_crop_dir = crop_dir + 'train/'
    val_crop_dir = crop_dir + 'val/'

    # generate train anno 
    for file_name in tqdm(os.listdir(train_crop_dir)):
        for img_name in os.listdir(str(train_crop_dir + file_name)):
            label = int(file_name)
            index = label_map[label]
            path = '/'.join(['train',file_name,img_name])
            anno = f'{path} {index}'
            train_anno.append(anno)
    train_txt_file.write_text('\n'.join(train_anno))

    # generate val anno 
    for file_name in tqdm(os.listdir(val_crop_dir)):
        for img_name in os.listdir(str(val_crop_dir + file_name)):
            label = int(file_name)
            index = label_map[label]
            path = '/'.join(['val',file_name,img_name])
            anno = f'{path} {index}'
            val_anno.append(anno)
    val_txt_file.write_text('\n'.join(val_anno))










    
