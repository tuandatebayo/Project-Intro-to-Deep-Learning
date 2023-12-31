# Project-Intro-to-Deep-Learning
## Requirements:
#### Python version 3.11.5
#### Libraries:
- ***ultralytics***
- ***pytorch*** version 2.1.2 with CUDA 11.8
- ***numpy***
- ***tqdm***

Install all required libraries by using the following cmd:
```pip install -r requirement.txt```
And clone this project to your pc by using the following cmd:
``` git clone https://github.com/tuandatebayo/Project-Intro-to-Deep-Learning.git ```
#### Data:
- Pascal VOC 2012 (trainval): ```http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar```
- Pascal VOC 2007 (test): ```https://github.com/ultralytics/yolov5/releases/download/v1.0/VOCtest_06-Nov-2007.zip```
For the data for yolov8, you should download our zip file in google drive (VOC2012Data.zip) or using our code (splittrainval, transformcoordinates) to transform the original dataset

## Training:
#### Yolov8
- Data preparing: Download ***VOC2012Data.zip*** in the given Google Drive or you can obtain the original dataset from the provided link above and utilize the ***splittrainval.py*** and ***transformcoordinates.py*** to convert the original dataset into a format suitable for YOLOv8.
- Take the file path of ***VOC2012Data.zip*** and put it in the variable ***zip_file_name*** in ***Train.ipynb***.
- Run the notebook ***Train.ipynb***.

#### SSD300
- Data preparing: Use the links above to download two datasets, then extract it to folder ***data*** in folder ***SSD300***.
- Download our trained model from Google Drive and put it in folder ***SSD300***
- Run the python file ***create_data_lists.py*** to prepare all the data path for training, validation and testing.
- Run the python file ***train.py*** to start training.

## Evaluation:
#### Yolov8
Run the notebook ***Val.ipynb***
#### SSD300
Run the python file ***evaluate.py***

## Infer:
#### Yolov8
- Put your image in the folder ***SampleImage*** and change the image file path in ***infer.py***
- Run the python file ***infer.py***

#### SSD300
- Put your image in the folder ***data*** in the folder ***SSD300***
- Change the variable ***img_path*** in the python file ***detect.py***
- Run the python file ***detect.py***