# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#PART 1
#Import the libraries 
import numpy as np
from PIL import Image,ImageFilter
import math

#import the noised image 
#img = Image.open("img.bmp")

def contrast(img):
    #transform the noised image into a matrix
    I=np.array(img)

    print(I.shape)
    n=I.shape[0] #LINES NUMBERS
    m=I.shape[1] #COLUMNS NUMBERS

    #PART 2 APPLICATION D CONTRAST
    n=I.shape[0] #LINES NUMBERS
    m=I.shape[1] #COLUMNS NUMBERS

    #create the new matrix of the smoothed image
    I2=np.ones([n,m])
    imin=np.min(I)
    imax=np.max(I)
    kmax=200
    kmin=10

    #apply the linear transformation filter 3X3 on blurred image 
    for u in range (1,n-1):
        for v in range (1,m-1):
            I2[u,v]=kmin+((kmax-kmin)/(imax-imin)*(I[u,v]-imin))
        
        #transformthe matrix into a image
        Img2=Image.fromarray(I2)
        if  Img2 != 'RGB' :
            Img2 = Img2.convert('RGB')
    
    # save the smoothed image
    Img2.save("contrast_enhancement.bmp")
    
    return Img2
    
    




#loading an image 
#image = Image.open('C:/Users/Dell Latitude E7240/Desktop/M1-S1/TIN/Casia v1/img.bmp')
#image.show()

#img = np.uint8(mpimg.imread('img.bmp'))

#img = np.uint8((0.2126* img[:,:,0]) + \
 #   np.uint8(0.7152 * img[:,:,1]) +\
  #       np.uint8(0.0722 * img[:,:,2]))

#def img_contrast(img):
 #  for x in range(img.size[0]):
  #     for y in range(img.size[1]):
   #        if (x, y) > 128:
    #          (r, g, b) = img.getpixel((x, y))
     #         img.putpixel((x, y), (r+80, g+80, b+80))
      #     else:
       #       if(x, y) < 128:
        #        (r, g, b) = img.getpixel((x, y))
         #            img.putpixel((x, y), (r-80, g-80, b-80))

#tam = img_contrast(img)

#plt.imshow(tam)


 
