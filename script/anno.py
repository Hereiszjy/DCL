import sys, shutil
from tqdm import tqdm, trange
import codecs
import os
import glob
import pandas as pd
from pathlib import Path

if __name__ == '__main__':
    crop_dir = '/data/disk3/cv2022/data/hpc_1973/'
    metadata_dir = '../datasets/HPC_US_1973'
    skulist = pd.read_csv("1973skus.csv")
    SKUID = skulist["ProductId"].unique().tolist()
    SKUID.sort()

    label_map = dict()
    for i in range(len(SKUID)):
        label_map[SKUID[i]] = i

    dataset_dir = Path(metadata_dir)
    train_txt_file = dataset_dir / 'ct_train.txt'
    val_txt_file = dataset_dir / 'ct_val.txt'
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










    
