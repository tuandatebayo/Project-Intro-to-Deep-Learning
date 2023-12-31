import os
#data path
train = r'VOCtrainval_11-May-2012\VOCdevkit\VOC2012\ImageSets\Main\train.txt'
val = r'VOCtrainval_11-May-2012\VOCdevkit\VOC2012\ImageSets\Main\val.txt'

#create folder
train_folder = r'train'
image_folder = r'train\images'
anno_folder = r'train\annos'
val_folder = r'valid'
imageval_folder = r'valid\images'
annoval_folder = r'valid\annos'
if not os.path.exists(train_folder):
    os.makedirs(train_folder)
if not os.path.exists(val_folder):
    os.makedirs(val_folder)
if not os.path.exists(image_folder):
    os.makedirs(image_folder)
if not os.path.exists(anno_folder):
    os.makedirs(anno_folder)
if not os.path.exists(imageval_folder):
    os.makedirs(imageval_folder)
if not os.path.exists(annoval_folder):
    os.makedirs(annoval_folder)
    
#copy image and anno
with open(train) as f:
    train_list = f.readlines()
with open(val) as f:
    val_list = f.readlines()
for i in train_list:
    i = i.strip()
    os.system('copy VOCtrainval_11-May-2012\VOCdevkit\VOC2012\JPEGImages\{}.jpg train\images\{}.jpg'.format(i,i))
    os.system('copy VOCtrainval_11-May-2012\VOCdevkit\VOC2012\Annotations\{}.xml train\annos\{}.xml'.format(i,i))
for i in val_list:
    i = i.strip()
    os.system('copy VOCtrainval_11-May-2012\VOCdevkit\VOC2012\JPEGImages\{}.jpg valid\images\{}.jpg'.format(i,i))
    os.system('copy VOCtrainval_11-May-2012\VOCdevkit\VOC2012\Annotations\{}.xml valid\annos\{}.xml'.format(i,i))
    
    
