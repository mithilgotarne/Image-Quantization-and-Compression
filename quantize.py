import numpy as np
from sklearn import cluster
from skimage import io
from sklearn.utils import shuffle
import sys
import os

def quantize(raster, k):
    width, height, depth = raster.shape
    reshaped_raster = np.reshape(raster, (width * height, depth))

    model = cluster.KMeans(n_clusters=k, n_jobs=-1)
    sample_raster = shuffle(reshaped_raster, random_state=0)[:1000]
    model.fit(sample_raster)
    labels = model.predict(reshaped_raster)
    palette = model.cluster_centers_

    quantized_raster = np.reshape(
        palette[labels], (width, height, palette.shape[1]))

    return quantized_raster / 255.0

directory = 'quantizedImages'
if not os.path.exists(directory):
    os.makedirs(directory)


image_filename = sys.argv[1]
k = int(sys.argv[2])

raster = io.imread(image_filename)
quantized_raster = quantize(raster, k)


if "/" in image_filename:
    image_filename = image_filename.split("/")[-1]
f, e = image_filename.split('.')
filename = f + '-' + str(k) + 'k.' + e

io.imsave(directory + '/' + filename, quantized_raster)