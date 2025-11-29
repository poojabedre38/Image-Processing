#image is a combination of pixels
'''pixels is a combination of RGB(red,green,blue)color'''
import cv2
#opening the image 
image = cv2.imread("./images.jpg")
rect_image=cv2.rectangle(image,(100,120),(220,270),[255,255,255],3)
#converting color
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blue_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGBA)

'''print(image)
print(image.ndim)
print(image.shape)'''
#showing image
cv2.imshow("blue ",blue_image)
cv2.imshow("image",image)
cv2.imshow("frame",gray_image)
while True:
    cv2.imshow("video",blue_image)
    cv2.waitKey(400)
    cv2.imshow("video",image)
    cv2.waitKey(400)
    cv2.imshow("video",gray_image)
    cv2.waitKey(400)
cv2.waitKey(0)

