import xml.etree.ElementTree as ET
import os

#get the path of the annotation
anno = r'VOC2012trainval\valid\annos'
label = r'VOC2012trainval\valid\labels'

os.makedirs(label, exist_ok=True)
#convert the box to the yolo format
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x, y, w, h)
def convert_cls(cls):
    if cls == 'aeroplane':
        return 0
    elif cls == 'bicycle':
        return 1
    elif cls == 'bird':
        return 2
    elif cls == 'boat':
        return 3
    elif cls == 'bottle':
        return 4
    elif cls == 'bus':
        return 5
    elif cls == 'car':
        return 6
    elif cls == 'cat':
        return 7
    elif cls == 'chair':
        return 8
    elif cls == 'cow':
        return 9
    elif cls == 'diningtable':
        return 10
    elif cls == 'dog':
        return 11
    elif cls == 'horse':
        return 12
    elif cls == 'motorbike':
        return 13
    elif cls == 'person':
        return 14
    elif cls == 'pottedplant':
        return 15
    elif cls == 'sheep':
        return 16
    elif cls == 'sofa':
        return 17
    elif cls == 'train':
        return 18
    elif cls == 'tvmonitor':
        return 19
    else:
        return -1
    
#get the box and name of the object from xml to txt in the yolo format
for filename in os.listdir(anno):
    if filename.endswith('.xml'):
        tree = ET.parse(os.path.join(anno, filename))
        root = tree.getroot()
        txt_file = os.path.join(label, os.path.splitext(filename)[0] + ".txt")
        f = open(txt_file, "w")
        for obj in root.iter('object'):
            cls = obj.find('name').text
            
            xmlbox = obj.find('bndbox')
            b = (int(xmlbox.find('xmin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymin').text), int(xmlbox.find('ymax').text))
            w = int(root.find('size').find('width').text)
            h = int(root.find('size').find('height').text)
            
            bb = convert((w, h), b)
            f.write(str(convert_cls(cls)) + " " + " ".join([str(a) for a in bb]) + '\n')
        f.close()
        