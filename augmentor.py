import glob
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
%matplotlib inline 
import cv2 as cv

#Note: input directory has sub-folders for separate class labels
#load image-paths from the input directory
def load_imgpath(dir_path):

    folders=glob.glob(dir_path+"*")     
    #print(folders) #print extracted file(img) names

    img_locs={} #store img location
    for i in folders:
        img_locs[ str(i[len(dir_path):]) ] = glob.glob(str(i)+"/*") #store paths of all images under respective class label
    #return a list having location of all information to be stored in csv format
    #print(img_locs)
    return img_locs
 
 
#load images from the extracted paths
def load_imgs(img_locs):

    dataset={}
    classes = list(img_locs.keys()) #extract class labels
        
    for i in range(len(classes)): 
        imgs=[]
        #load images in each class label
        for imgloc in img_locs[ classes[i] ] : 
            img=cv.imread( imgloc , 0 ) #0 reads image in grayscale format
            img=img[...,None]           #reshape img as array of dim (n,n,1)
            imgs.append(img)            
        #print(np.array(imgs).shape)    #verify number of samples extracted
        dataset[classes[i]] = imgs

    #print(dataset)
    return dataset
    
 
#rotate image by the specified angle
def rotate_image(image, angle ):
    img_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv.getRotationMatrix2D(img_center, angle, 1.0)
    rotated = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
    return rotated


#rotates cell by specified angle, and masks it with image background to retain original shape
def img_augmentor(image, angle):
    
    #background mask
    bgmask=np.zeros((image.shape[:2]), np.uint8)
    cv.circle(bgmask, ( int(bgmask.shape[0]/2), int(bgmask.shape[1]/2) ), 32, (255), -1)
    
    #cell mask
    cellmask=cv.bitwise_not(bgmask)
    
    #cell background
    bg = cv.bitwise_or(image, image, mask=cellmask)
    
    #rotate img
    rotated=rotate_image(image, angle)
    
    #cell cropping
    cell= cv.bitwise_or(rotated, rotated, mask=bgmask)
    final = cv.bitwise_or(bg, cell)
    
    #disp
    #cv.imshow("final mask", final)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    
    return final
    

#run the code
#sample directory : img_dataset

img_locs=load_imgpath(dir_path="img_dataset/") #

dataset=load_imgs(img_locs)

classes = list(img_locs.keys())

#iterate over images in all class labels
for i in range(len(classes)):
    
    filename = "augmented_"+classes[i]+".csv"      
          
    for image in dataset[ classes[i] ]:
        
        #rotate image at 10 degree increments
        for angle in np.arange(0, 360, 10): 
            
            aug_img = img_augmentor(image, angle)
            #uncomment to display the sample image
            #cv.imshow("final mask", img_array)
            #cv.waitKey(0)
            #cv.destroyAllWindows()
            
						aug_img = (aug_img.flatten()) #convert to 1-d array, so each row in the csv will be an image
            aug_img  = aug_img.reshape(-1, 1).T

            with open(filename, 'ab') as f:  #save image in a csv file
                np.savetxt(f, aug_img, delimiter=",")     
