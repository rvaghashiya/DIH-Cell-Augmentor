# DIH-Cell-Augmentor
A setup for augmentation of biological cells captured via Digital Inline Holography

# Method
* Load dataset, having images grouped under labels
* Augment cell sample by rotation at specific angle
* Store augmented images in a csv

# Augmentation Procedure
* Create a mask to extract the cell background
* Negate the above mask to extract the cell 
* Rotate the image by specified degree, achieved via `getRotationMatrix2D` and `warpAffine` functions in cv2
* Extract the rotated cell signature using the negated mask
* Mask it with the extracted cell background to create an augmented image, with same shape as original image

Note: The code is applicable only for augmentation of objects/cells lying within the maximum fitting circle which can be fit into the image

# Pre-requisites:
* cv2
* glob, or alternatively use os
* numpy

# Demo:
Note: Black dot has been added for easier vizualization

## Input Image: 
<img src="images/original.jpg" width=100 >

## Augmented Images:
Augmented Images on rotation by 0, 10, 20, 30,.....,350 degrees :


|   |     |   |
|------------|-------------|
| <img src="images/aug_img_0.jpg" width=100 >  | <img src="images/aug_img_10.jpg" width=100 > | <img src="images/aug_img_20.jpg" width=100 > |
| <img src="images/aug_img_30.jpg" width=100 > | <img src="images/aug_img_40.jpg" width=100 > | <img src="images/aug_img_50.jpg" width=100 > |
| <img src="images/aug_img_60.jpg" width=100 > | <img src="images/aug_img_70.jpg" width=100 > | <img src="images/aug_img_80.jpg" width=100 > | 
| <img src="images/aug_img_90.jpg" width=100 > | <img src="images/aug_img_100.jpg" width=100 > | <img src="images/aug_img_110.jpg" width=100 > |
| <img src="images/aug_img_120.jpg" width=100 > | <img src="images/aug_img_130.jpg" width=100 > | <img src="images/aug_img_140.jpg" width=100 > |
| <img src="images/aug_img_150.jpg" width=100 > | <img src="images/aug_img_160.jpg" width=100 > | <img src="images/aug_img_170.jpg" width=100 > |
| <img src="images/aug_img_180.jpg" width=100 > | <img src="images/aug_img_190.jpg" width=100 > | <img src="images/aug_img_200.jpg" width=100 > |
| <img src="images/aug_img_210.jpg" width=100 > | <img src="images/aug_img_220.jpg" width=100 > | <img src="images/aug_img_230.jpg" width=100 > |
| <img src="images/aug_img_240.jpg" width=100 > | <img src="images/aug_img_250.jpg" width=100 > | <img src="images/aug_img_260.jpg" width=100 > |
| <img src="images/aug_img_270.jpg" width=100 > | <img src="images/aug_img_280.jpg" width=100 > | <img src="images/aug_img_290.jpg" width=100 > |
| <img src="images/aug_img_300.jpg" width=100 > | <img src="images/aug_img_310.jpg" width=100 > | <img src="images/aug_img_320.jpg" width=100 > |
| <img src="images/aug_img_330.jpg" width=100 > | <img src="images/aug_img_340.jpg" width=100 > | <img src="images/aug_img_350.jpg" width=100 > |
