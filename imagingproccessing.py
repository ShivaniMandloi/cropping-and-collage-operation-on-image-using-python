#importing modules
import cv2, numpy

#task 4.1: Create your own image
#Creating Image_1

img_1= numpy.zeros((600, 600, 3),numpy.uint8)
cv2.circle(img_1,(75, 75), 106, (240, 128, 128), -1)
cv2.circle(img_1,(225, 225), 106, (240, 128, 128), -1)
cv2.circle(img_1,(375, 375), 106 , (240, 128, 128), -1)
cv2.circle(img_1,(525, 525), 106 , (240, 128, 128), -1)

cv2.imshow('image_1_before',img_1)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#Creating Image_2

img_2= numpy.ones((600, 600, 3),numpy.uint8)*255
cv2.circle(img_2,(525, 75), 106, (240, 128, 128), -1)
cv2.circle(img_2,(375, 225), 106, (240, 128, 128), -1)
cv2.circle(img_2,(225, 375), 106 , (240, 128, 128), -1)
cv2.circle(img_2,(75, 525), 106 , (240, 128, 128), -1)

cv2.imshow('image_2_before',img_2)
cv2.waitKey(700)
cv2.destroyAllWindows()

#Task 4.2: Crop some part of both image and swap it

#Creating a temporary array for swapping
temp=numpy.zeros((600, 600, 3),numpy.uint8)

for i in range(150,450):
    for j in range(150, 450):
        temp[i,j]= img_2[i,j]
        img_2[i,j]=img_1[i,j]
        img_1[i,j]=temp[i,j]
        
#swapped image_1
cv2.imshow('image_1_swapped',img_1)
cv2.waitKey(700)
cv2.destroyAllWindows()        

#swapped image_2
cv2.imshow('image_2_swapped',img_2)
cv2.waitKey(700)
cv2.destroyAllWindows()

#Task 4.3: Create a collage of both the images
image= numpy.append(img_1,img_2,axis=1)

cv2.imshow('image_com',image)
cv2.waitKey(700)
cv2.destroyAllWindows()
