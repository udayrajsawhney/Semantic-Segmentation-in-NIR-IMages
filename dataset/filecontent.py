import os 
from pprint import pprint 

files = []
for dirname, dirnames, filenames in os.walk('/Users/udaysawhney/Desktop/segmentation/deeplab_v3-master/dataset/create_dataset/nirscene1'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        files.append(subdirname)

    # print path to all filenames.
    # for filename in filenames:
    #     files.append(os.path.join(dirname, filename))


pprint(files)

