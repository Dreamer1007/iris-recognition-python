import numpy as np
from PIL import Image

# create our own histogram function
def get_histogram(image, bins):
    # array with size of bins, set to zeros
    histogram = np.zeros(bins)
    
    # loop through pixels and sum up counts of pixels
    for pixel in image:
        histogram[pixel] += 1
    
    # return our final result
    return histogram


# create our cumulative sum function
def cumsum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)        

def histogram_equalization(img):

    # put pixels in a 1D array by flattening out img array
    flat = img.flatten()

    # execute our histogram function
    hist = get_histogram(flat, 256)

    # execute the fn
    cs = cumsum(hist)

    # numerator & denomenator
    nj = (cs - cs.min()) * 255
    N = cs.max() - cs.min()

    # re-normalize the cumsum
    cs = nj / N 

    # cast it back to uint8 since we can't use floating point values in images
    cs = cs.astype('uint8')

    # get the value from cumulative sum for every index in flat, and set that as img_new
    img_new = cs[flat]

    # put array back into original shape since we flattened it
    img_new = np.reshape(img_new, img.shape)

    return img_new