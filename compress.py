import numpy as np
from sklearn.decomposition import PCA
from skimage import io
import sys
import os

def compress(raster, pca_components):
    pca = PCA(n_components=pca_components)
    for i in range(raster.shape[2]):
        pca.fit(raster[:,:,i])
        compressed_raster = pca.transform(raster[:,:,i])
        raster[:,:,i] = pca.inverse_transform(compressed_raster)
        
    return raster

directory = 'compressedImages'
if not os.path.exists(directory):
    os.makedirs(directory)


image_filename = sys.argv[1]
pca_components = int(sys.argv[2])
raster = io.imread(image_filename)
compressed_raster = compress(raster, pca_components)

if "/" in image_filename:
    image_filename = image_filename.split("/")[-1]
f, e = image_filename.split('.')
filename = f + '-' + str(pca_components) + 'pca.' + e

io.imsave(directory + '/' + filename, compressed_raster)