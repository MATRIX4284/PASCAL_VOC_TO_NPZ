import argparse
import os
import xml.etree.ElementTree as ElementTree
import numpy as np
from PIL import Image

classes = [
    "cat","dog"
]

parser = argparse.ArgumentParser(
    description='Convert any Pascal VOC Annotated dataset to npz.')
parser.add_argument(
    '-i',
    '--path_to_voc_image',
    help='path to VOCdevkit Image directory',
    default='./Image_files/')
parser.add_argument(
    '-a',
    '--path_to_voc_annotation',
    help='path to VOCdevkit Annotation directory',
    default='./Annotations/')
parser.add_argument(
    '-v',
    '--path_to_voc',
    help='path to VOCdevkit Annotation directory',
    default='./')

parser.add_argument(
    '-o',
    '--path_to_output_npz',
    help='path to VOCdevkit Annotation directory',
    default='./Output/')


def get_boxes_for_id(box_element_path):
  
    fname = os.path.join(box_element_path)
    with open(fname) as in_file:
        xml_tree = ElementTree.parse(in_file)
    root = xml_tree.getroot()
    boxes = []
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        label = obj.find('name').text
        if label not in classes or int(
                difficult) == 1:  # exclude difficult or unlisted classes
            continue
        xml_box = obj.find('bndbox')
        bbox = (classes.index(label), int(xml_box.find('xmin').text),
                int(xml_box.find('ymin').text), int(xml_box.find('xmax').text),
                int(xml_box.find('ymax').text))
        boxes.extend(bbox)
    return np.array(
        boxes)  


def add_to_dataset(voc_image_path, voc_annotation_path,npz_output_path):
    
    filelist = sorted(os.listdir(voc_image_path))
    #print(filelist)
    images = np.array([np.array(Image.open(os.path.join(voc_image_path,fname))) for fname in filelist])
    print(images.shape)
    print(images.dtype)
    
    box_list = sorted(os.listdir(voc_annotation_path))
    boxes = np.array([np.array(get_boxes_for_id(os.path.join(voc_annotation_path,bname))) for bname in box_list])

    
    print(boxes.shape)
    print(boxes.dtype)
    np.savez(npz_output_path+'dogs_cats.npz', images, boxes)
    return 1


def _main(args):
    voc_image_path = os.path.expanduser(args.path_to_voc_image)
    voc_annotation_path = os.path.expanduser(args.path_to_voc_annotation)
    voc_path = os.path.expanduser(args.path_to_voc)
    npz_output_path = os.path.expanduser(args.path_to_output_npz)
    total_train_ids = len(os.listdir(voc_image_path))

    
    add_to_dataset(
        voc_image_path,
        voc_annotation_path,
        npz_output_path
        )

if __name__ == '__main__':
    _main(parser.parse_args())
