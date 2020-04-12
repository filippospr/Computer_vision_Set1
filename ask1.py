import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
from sys import argv



def thresholding(input_image,output_image,threshold):
    img_in=np.array(Image.open(input_image))
    length=len(img_in)
    width=len(img_in[0])
    k=int(threshold)
    rgb=False
    
    if len(img_in.shape)>2:
        img_in=rgb2gray(img_in,length,width)
        rgb=True

    for i in range(0,length):
        for j in range(0,width):
            if img_in[i][j]>k:
                img_in[i][j]=255
            else:
                img_in[i][j]=0
    
    
    #If our picture was in rgb form we need to need to convert it as was
    #before after finishing thresholding

    if rgb :
        img_out=Image.fromarray(img_in).convert('RGB')
    else :
        img_out=Image.fromarray(img_in)
    # save the image
    img_out.save(output_image)

    plt.imshow(img_in,cmap="gray")
    plt.title("Threshold=%d" %k)
    plt.show()


#convert an rgb image into a grayscale image using the median of the RGB value
def rgb2gray(input_image_array,length,width):
    output_array=np.zeros((length,width),dtype=np.int)

    for i in range(0,length):
        for j in range(0,width):
            median_rgb=0
            for k in range(0,3):
                median_rgb+=input_image_array[i][j][k]
            median_rgb=median_rgb/3
            output_array[i][j]=median_rgb

    return output_array    


thresholding(argv[1],argv[2],argv[3])