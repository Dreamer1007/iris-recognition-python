#import needed libraries
import numpy as np
from PIL import Image,ImageFilter 
import math

#import the noised image 
#img = Image.open("img.bmp")

def lissage(img):
    #transform the noised image into a matrix 
    I=np.array(img)

    print(I.shape)
    n=I.shape[0] #lines numbers
    m=I.shape[1] #columns numbers

    #/////////PART1 ***** REMPLISSAGE DE L'IMAGE ****** ///////
    collone1=np.array([I[:,0]]).T
    collone2=np.array([I[:,m-1]]).T
    I= np.c_[collone1,I,collone2]#ajout des 2 collones
    ligne1=np.array([I[0,:]])
    ligne2=np.array([I[n-1,:]])
    I= np.r_[ligne1,I,ligne2]    #ajout des 2 lignes
    print(I.shape)

    #transform the matrix to an image remplit
    Img2=Image.fromarray(I)

    #/////////PART2 ***** APPICATION DU FILTRE MEAN ****** ///////
    n=I.shape[0] #lines numbers
    m=I.shape[1] #columns numbers

    #create the new matrix of the smoothed image
    I2=np.ones([n,m])

    #apply the linear transformation filter 3x3 on blurred image 
    for u in range(1,n-1):       
        for v in range(1,m-1): 
            I2[u,v]=(((1/9)*I[u,v-1])+((1/9)*I[u,v])+((1/9)*I[u,v+1])+((1/9)*I[u-1,v-1])+((1/9)*I[u-1,v])+((1/9)*I[u-1,v+1])+((1/9)*I[u+1,v-1])+((1/9)*I[u+1,v])+((1/9)*I[u+1,v+1]))
         
            #transform the matrix to an image smoothed
            Img2=Image.fromarray(I2)
            if Img2 != 'RGB':
                Img2 = Img2.convert('RGB')
    
    #save the smoothed image 
    #Img2.save("filtre_moyenne.bmp")

    #/////////PART3 ***** TRIMMING IMAGE  ****** ///////
    #supprimer le ligne et colonne ajouter au debut pour appliquer le lissage
    I2=np.delete(I2, 0, axis = 1)
    I2=np.delete(I2, I2.shape[1]-1, axis = 1)
    I2=np.delete(I2, 0, axis = 0)
    I2=np.delete(I2, I2.shape[0]-1, axis = 0)
    Img3=Image.fromarray(I2)
    
    if Img3 != 'RGB':
        Img3 = Img3.convert('RGB')
    
    #save the smoothed image after trimming
    Img3.save("lissage.bmp")
    return I2
