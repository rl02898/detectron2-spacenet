import os
import json
import geojson
import numpy as np
import pandas as pd

from osgeo import gdal
from sklearn.model_selection import train_test_split

# custom functions
from utils.functions import grab_certain_file, tif_to_png


RANDOM_SEED = 560

# Path to all images
rio_train = "Spacenet/AOI_1_Rio_Train/RGB-PanSharpen"
rio_test = "Spacenet/AOI_1_Rio_Test_public/RGB-PanSharpen"

vegas_train = "Spacenet/AOI_2_Vegas_Train/RGB-PanSharpen"
vegas_test = "Spacenet/AOI_2_Vegas_Test_public/RGB-PanSharpen"

paris_train = "Spacenet/AOI_3_Paris_Train/RGB-PanSharpen"
paris_test = "Spacenet/AOI_3_Paris_Test_public/RGB-PanSharpen"

shanghai_train = "Spacenet/AOI_4_Shanghai_Train/RGB-PanSharpen"
shanghai_test = "Spacenet/AOI_4_Shanghai_Test_public/RGB-PanSharpen"

khartoum_train = "Spacenet/AOI_5_Khartoum_Train/RGB-PanSharpen"
khartoum_test = "Spacenet/AOI_5_Khartoum_Test_public/RGB-PanSharpen"



# Convert TIFF to PNG
# Rio de Janeiro
rio_images = grab_certain_file(".tif", rio_train)
train, val = train_test_split(rio_images, test_size=0.2, random_state=RANDOM_SEED)
test = grab_certain_file(".tif", rio_test)

tif_to_png(train, rio_train, "Spacenet/train")
print("Done converting Rio/train images")
tif_to_png(val, rio_train, "Spacenet/val")
print("Done converting Rio/val images")
tif_to_png(test, rio_test, "Spacenet/test")
print("Done converting Rio/test images")

# Vegas
vegas_images = grab_certain_file(".tif", vegas_train)
train, val = train_test_split(vegas_images, test_size=0.2, random_state=RANDOM_SEED)
test = grab_certain_file(".tif", vegas_test)

tif_to_png(train, vegas_train, "Spacenet/train", normalize=True)
print("Done converting Vegas/train images")
tif_to_png(val, vegas_train, "Spacenet/val", normalize=True)
print("Done converting Vegas/val images")
tif_to_png(test, vegas_test, "Spacenet/test", normalize=True)
print("Done converting Vegas/test images")

# Paris
paris_images = grab_certain_file(".tif", paris_train)
train, val = train_test_split(paris_images, test_size=0.2, random_state=RANDOM_SEED)
test = grab_certain_file(".tif", paris_test)

tif_to_png(train, paris_train, "Spacenet/train", normalize=True)
print("Done converting Paris/train images")
tif_to_png(val, paris_train, "Spacenet/val", normalize=True)
print("Done converting Paris/val images")
tif_to_png(test, paris_test, "Spacenet/test", normalize=True)
print("Done converting Paris/test images")

# Shanghai
shanghai_images = grab_certain_file(".tif", shanghai_train)
train, val = train_test_split(shanghai_images, test_size=0.2, random_state=RANDOM_SEED)
test = grab_certain_file(".tif", shanghai_test)

tif_to_png(train, shanghai_train, "Spacenet/train", normalize=True)
print("Done converting Shanghai/train images")
tif_to_png(val, shanghai_train, "Spacenet/val", normalize=True)
print("Done converting Shanghai/val images")
tif_to_png(test, shanghai_test, "Spacenet/test", normalize=True)
print("Done converting Shanghai/test images")

# Khartoum
khartoum_images = grab_certain_file(".tif", khartoum_train)
train, val = train_test_split(khartoum_images, test_size=0.2, random_state=RANDOM_SEED)
test = grab_certain_file(".tif", khartoum_test)

tif_to_png(train, khartoum_train, "Spacenet/train", normalize=True)
print("Done converting Khartoum/train images")
tif_to_png(val, khartoum_train, "Spacenet/val", normalize=True)
print("Done converting Khartoum/val images")
tif_to_png(test, khartoum_test, "Spacenet/test", normalize=True)
print("Done converting Khartoum/test images")
