# PASCAL_VOC_TO_NPZ

Installation:
sudo apt-get install pyqt5-dev-tools
sudo pip3 install lxml
make qt5py3

Using the tool:

Go to folder.

cd labelImg-master
python3 labelImg.py
python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

Using the PASCAL VOC To NPZ conversion tool.
1.Convert any PASCAL VOC Annotated File to Numpy Zip Format to get Data Ready for Training  YOLOV2 Object Recognition
Keep Your Image files inside the folder Image_files and Annotation .xml in the folder Annotations.

2.Run the following commands:

cd VOC_ANNO_NPZ
python3 VOC_TO_NPZ.py '-i'/'--path_to_voc_image'  '-a'/'--path_to_voc_annotation' '-v'/'--path_to_voc'  '-o'/'--path_to_output_npz'
python3 VOC_TO_NPZ.py 
The result npz file will be formed in the folder:
File Name: 
[Output_name].npz

Output_name is name of the output file you will provide




