import cv2
import numpy as np

def dec_to_bin(x):
	return (bin(x)[2:].zfill(8))

pt = raw_input("Enter the message to be encrypted in the image");
pt+='!'
length = len(pt)

k=0
#print len(dec_to_bin(10))

image=cv2.imread('images.jpg',-1)

#To determine size of the image
mat=image.shape
height = mat[0]
width = mat[1]

for i in range(0,height):

	for j in range (0,width):

		if k==length:
			break
		temp = pt[k]
		tem = ord(temp)
		st = dec_to_bin(tem)
		pixel = image[i,j]
		#print pixel

		pixel2 = dec_to_bin(pixel[2])

		pix=""
		for ff in range(0,5):
			pix+=pixel2[ff]
		pix+=st[5]
		pix+=st[6]
		pix+=st[7]
		px2=int(pix,2)

		pixel1 = dec_to_bin(pixel[1])
		pix=""
		for ff in range(0,5):
			pix+=pixel1[ff]
		pix+=st[2]
		pix+=st[3]
		pix+=st[4]
		px1=int(pix,2)

		pixel0 = dec_to_bin(pixel[0])
		pix=""
		for ff in range(0,6):
			pix+=pixel0[ff]
		pix+=st[0]
		pix+=st[1]
		px0=int(pix,2)

		image[i,j]=[px0,px1,px2]
		#print i,j,image[i,j]
		k=k+1


cv2.imwrite('encrypted.png',image)
#cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()