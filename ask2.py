import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
from sys import argv
import math

#Nearest neighbor interpolation is not completed



#matrix  to perform affine transformation 
t_affine=np.zeros((3,3))
t_affine[0][0]=argv[3]
t_affine[0][1]=argv[4]
t_affine[0][2]=argv[5]
t_affine[1][0]=argv[6]
t_affine[1][1]=argv[7]
t_affine[1][2]=argv[8]
t_affine[2][2]=1



def affine_transform(t_affine,input_image,output_image):
    #open input image
    img_in=np.array(Image.open(input_image))
    height=len(img_in)
    width=len(img_in[0])

    img_out=np.zeros((height,width),dtype=np.int)
    
    #We use the offset variables so that i can move the center(0,0) of the image  
    x_offset=math.floor(width/2)
    y_offset=math.floor(height/2)

    for i in range(height):
        for j in range(width):
            # transform thecoordinates of the pixel so that we can 
            #have the (0,0) point int the center of the image
            x_old=j-x_offset
            y_old=y_offset-i

            x_new=int(t_affine[0][0]*x_old+t_affine[0][1]*y_old+t_affine[0][2])
            y_new=int(t_affine[1][0]*x_old+t_affine[1][1]*y_old+t_affine[1][2])
            
            #if the new coordinates of a point are outside the new image then continue
            if abs(int(y_new-y_offset)) >=height or abs(int(x_new+x_offset))>=width:
                continue
            
            #we do the reverse transform to read the pixels from img
            img_out[abs(int(y_new-y_offset))][abs(int(x_new+x_offset))]=img_in[abs(int(y_old-y_offset))][abs(int(x_old+x_offset))]
    
    plt.imshow(img_out,cmap="gray")
    plt.show()


affine_transform(t_affine,argv[1],argv[2])
