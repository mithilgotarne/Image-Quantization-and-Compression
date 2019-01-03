# Image Quantization using Kmeans and Image compression using PCA

## Pre-requsite:
Make sure you have [anaconda](https://www.anaconda.com/), [scikit-learn](https://scikit-learn.org/stable/install.html) and [scikit-image](https://scikit-image.org/download)  

## 1. Color Quantization

Used kmeans clustering to create centroid from sample of 1000 points in image array / raster. Then predicted center for each point in the raster and ploted them which resulted in quantized image of the original image

### How to Run:

1. run `python quantize.py <imagefilePath> <valueOfK>`
    
    example `python quantize.py images/image3.jpg 32`

### Output:

- Output images are stored in folder `quantizedImages` as `filename-<kvalue>k.jpg`

### Report:


Image | Original File Size | Value of k used | Image Quality | Image Size
-|-|-|-|-
 Image1 | 355.4K | 2 | Just two colors visible sort of black and light blue  | 302.4K
 Image1 | 355.4K | 8 | Some color details missing in the sky  | 334K
 Image1 | 355.4K | 16 | Almost similar  | 334.4K
 Image2 | 536.6K | 8 | Object edges are blur  | 292.1K
 Image2 | 536.6K | 16 | Blur dark colors  | 296.9K
 Image2 | 536.6K | 64 | Almost similar  | 285.9K
 Image3 | 598.4k | 16 | Blur  | 402.4k
 Image3 | 598.4k | 32 | Less Blur  | 411.6K
 Image3 | 598.4k | 64 | Almost similar  | 414.3K

### References
- [https://scikit-learn.org/stable/auto_examples/cluster/plot_color_quantization.html](https://scikit-learn.org/stable/auto_examples/cluster/plot_color_quantization.html)
- [https://en.wikipedia.org/wiki/Color_quantization](https://en.wikipedia.org/wiki/Color_quantization)
- [https://lmcaraig.com/color-quantization-using-k-means/](https://lmcaraig.com/color-quantization-using-k-means/)
- [https://appliedmachinelearning.blog/2017/03/08/image-compression-using-k-means-clustering/](https://appliedmachinelearning.blog/2017/03/08/image-compression-using-k-means-clustering/)

## 2. PCA for Images

Ran PCA with different number of components. Transformed input array of every color channel i.e. for Red, Green and Blue into pca components. Then inverse transformed pca components to array. Plotted this arrays of all channel to for compressed images.

### How to Run:

1. cd into `path/to/partIII`
2. run `python compress.py <imagefilePath> <valueOfPrincipalComponents>`
    
    example `python compress.py images/image3.jpg 100`

### Output:

- Output images are stored in folder `compressedImages` as `filename-<pcvalue>pca.jpg`

### Report:


Image | Original File Size | Value of Principal Components | Image Quality | Image Size
-|-|-|-|-
 Image1 | 355.4K | 100 | Multi-colored noise  | 480.1K
 Image1 | 355.4K | 150 | Multi-colored noise  | 514.1K
 Image1 | 355.4K | 200 | Multi-colored noise  | 532.1K
 Image2 | 536.6K | 150 | Noise in white color  | 292.1K
 Image2 | 536.6K | 200 | Less Noise in white color | 296.9K
 Image2 | 536.6K | 500 | Almost similar with un-noticable noise in white color  | 285.9K
 Image3 | 598.4k | 800 | Hazy with noise in white color  | 402.4k
 Image3 | 598.4k | 1000 | Hazy  | 411.6K
 Image3 | 598.4k | 1200 | Almost similar to original  | 414.3K

### References
- [http://people.ciirc.cvut.cz/~hlavac/TeachPresEn/11ImageProc/15PCA.pdf](http://people.ciirc.cvut.cz/~hlavac/TeachPresEn/11ImageProc/15PCA.pdf)
- [http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1679-45082012000200004](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1679-45082012000200004)
- [http://dilloncamp.com/projects/pca.html](http://dilloncamp.com/projects/pca.html)
