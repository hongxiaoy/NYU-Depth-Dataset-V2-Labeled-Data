import h5py
import numpy as np
import pandas as pd
import pickle


path = 'nyu_depth_v2_labeled.mat'
labeled_data = h5py.File(path)


nyu_depth_v2_labeled_data = {}


# 1 accelData
print("Processing accelData:", end=' ')
accelData = labeled_data['accelData'][:]
nyu_depth_v2_labeled_data['accelData'] = accelData.T 
print(accelData.T.shape)                    # (1449, 4)


# 2 depths
print("Processing depths:", end=' ')
depths = labeled_data['depths'][:]
nyu_depth_v2_labeled_data['depths'] = np.moveaxis(depths, 1, 2)
print(np.moveaxis(depths, 1, 2).shape)      # (1449, 480, 640)


# 3 images
print("Processing images:", end=' ')
images= labeled_data['images'][:]
nyu_depth_v2_labeled_data['images'] = np.moveaxis(images, 2, 3)
print(np.moveaxis(images, 2, 3).shape)      # (1449, 3, 480, 640)


# 4 instances
print("Processing instances:", end=' ')
instances = labeled_data['instances'][:]
nyu_depth_v2_labeled_data['instances'] = np.moveaxis(instances, 1, 2)
print(np.moveaxis(instances, 1, 2).shape)   # (1449, 480, 640)


# 5 labels
print("Processing labels:", end=' ')
labels = labeled_data['labels'][:]
nyu_depth_v2_labeled_data['labels'] = np.moveaxis(labels, 1, 2)
print(np.moveaxis(labels, 1, 2).shape)      # (1449, 480, 640)


# 6 names
print("Processing names:", end=' ')
names = labeled_data['names'][:]
names_list = []
for i in range(names.shape[1]):
    name = ''.join(chr(j) for j in labeled_data[names[0][i]])
    names_list.append(name)
nyu_depth_v2_labeled_data['names'] = names_list
print(len(names_list))


# 7 namesToIds
print("Processing namesToIds:", end=' ')
namesToIds_dict = {}
names2ids = pd.read_csv('names2ids.csv', header=None)
for k, v in zip(names2ids.iloc[:][0], names2ids.iloc[:][1]):
    namesToIds_dict[k.strip('\'')] = v
nyu_depth_v2_labeled_data['namesToIds'] = namesToIds_dict
print(len(namesToIds_dict))


# 8 rawDepths
print("Processing rawDepths:", end=' ')
rawDepths = labeled_data['rawDepths'][:]
nyu_depth_v2_labeled_data['rawDepths'] = np.moveaxis(rawDepths, 1, 2)
print(np.moveaxis(rawDepths, 1, 2).shape)   # (1449, 480, 640)


# 9 rawDepthFilenames
print("Processing rawDepthFilenames:", end=' ')
rawDepthFilenames = labeled_data['rawDepthFilenames'][:]
rawDepthFilenames_list = []
for i in range(rawDepthFilenames.shape[1]):
    rawDepthFilename = ''.join(chr(j) for j in labeled_data[rawDepthFilenames[0][i]])
    rawDepthFilenames_list.append(rawDepthFilename)
nyu_depth_v2_labeled_data['rawDepthFilenames'] = rawDepthFilenames_list
print(len(rawDepthFilenames_list))


# 10 rawRgbFilenames
print("Processing rawRgbFilenames:", end=' ')
rawRgbFilenames = labeled_data['rawRgbFilenames'][:]
rawRgbFilenames_list = []
for i in range(rawRgbFilenames.shape[1]):
    rawRgbFilename = ''.join(chr(j) for j in labeled_data[rawRgbFilenames[0][i]])
    rawRgbFilenames_list.append(rawRgbFilename)
nyu_depth_v2_labeled_data['rawRgbFilenames'] = rawRgbFilenames_list
print(len(rawRgbFilenames_list))


# 11 scenes
print("Processing scenes:", end=' ')
scenes = labeled_data['scenes'][:]
scenes_list = []
for i in range(scenes.shape[1]):
    scene = ''.join(chr(j) for j in labeled_data[scenes[0][i]])
    scenes_list.append(scene)
nyu_depth_v2_labeled_data['scenes'] = scenes_list
print(len(scenes_list))


# 12 sceneTypes
sceneTypes = labeled_data['sceneTypes'][:]
print("Processing sceneTypes:", end=' ')
sceneTypes_list = []
for i in range(sceneTypes.shape[1]):
    sceneType = ''.join(chr(j) for j in labeled_data[sceneTypes[0][i]])
    sceneTypes_list.append(sceneType)
nyu_depth_v2_labeled_data['sceneTypes'] = sceneTypes_list
print(len(sceneTypes_list))


with open('nyu_depth_v2_labeled_data.pkl', 'wb') as f:
    pickle.dump(nyu_depth_v2_labeled_data, f)
