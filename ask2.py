import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
from sys import argv
import math
# import cv2


# img=cv2.resize(imgin,300,650)




#matrix  to perform affine transformation 
t_affine=np.zeros((3,3))
t_affine[0][0]=argv[3]
t_affine[0][1]=argv[4]
t_affine[0][2]=argv[5]
t_affine[1][0]=argv[6]
t_affine[1][1]=argv[7]
t_affine[1][2]=argv[8]
t_affine[2][2]=1


# t_affine=[argv[3],argv[4],argv[5],argv[6],argv[7],argv[8],0,0,1]


def affine_transform(t_affine,input_image,output_image):
    img_in=np.array(Image.open(input_image))
    print(img_in)
    height=len(img_in)
    width=len(img_in[0])
    print(width)
    print(height)
    img_out=np.zeros((height,width))
    
    x_offset=math.floor(width/2)
    y_offset=math.floor(height/2)

    for i in range(height):
        for j in range(width):
            # transform thecoordinates of the pixel so that we can 
            #have the (0,0) point int the center of the image
            x_old=j-x_offset
            #to see
            y_old=y_offset-i
            x_new=t_affine[0][0]*x_old+t_affine[0][1]*y_old+t_affine[0][2]
            y_new=t_affine[1][0]*x_old+t_affine[1][1]*y_old+t_affine[1][2]
            

            if abs(int(y_new-y_offset)) >=height or abs(int(x_new+x_offset))>=width:
                continue
            # print("Coordinates: %d %d \n"%(abs(int(y_old-y_offset)),abs(int(x_old+x_offset))))
            #we do the reverse transform to read the pixels from img
            img_out[abs(int(y_new-y_offset))][abs(int(x_new+x_offset))]=img_in[abs(int(y_old-y_offset))][abs(int(x_old+x_offset))]
    # img_out=nn_interpolate(img_out,1)
    # for i in range(height):
        # for j in range(width):
            # if math.floor(i/t_affine[1][1])>=height or math.floor(j/t_affine[0][0])>=width:
                # continue
            # img_out[i][j]=img_in[math.floor(i/t_affine[1][1])][math.floor(j/t_affine[0][0])]
    
    plt.imshow(nn_interpolate(img_out,1),cmap="gray")
    plt.show()


# Nearest neighbor interpolation 
def nn_interpolate(image, scale_factor):

	# Extract size
	(rows, cols) = image.shape
	scaled_height = rows * scale_factor
	scaled_weight = cols * scale_factor

	# Compute ratio
	row_ratio = rows / scaled_height
	col_ratio = cols / scaled_weight

	row_position = np.floor(np.arange(scaled_height) * row_ratio).astype(int)
	column_position = np.floor(np.arange(scaled_weight) * col_ratio).astype(int)
	
	# Initialize scaled image
	scaled_image = np.zeros((scaled_height, scaled_weight), np.uint8)

	for i in range(scaled_height):
		for j in range(scaled_weight):
			scaled_image[i, j] = image[row_position[i], column_position[j]]

	return scaled_image
affine_transform(t_affine,argv[1],argv[2])
"""
arr=np.zeros((101,201),dtype=int)
x_offset=math.floor(len(arr)/2)
y_offset=math.floor(len(arr[0])/2)
counter=0
for i in range(len(arr)):
    for j in rangelen(arr[0])):
        arr[i][j]=counter-offset
        counter+=1
    counter=0
print(arr)
"""