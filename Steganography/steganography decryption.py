import cv2
import numpy as np

def dec_to_bin(x):
	return (bin(x)[2:].zfill(8))

image = cv2.imread('encrypted.png',-1)

#To determine size of the image
mat = image.shape
height = mat[0]
width = mat[1]

ans = ""
tte=0

k=0
for i in range(0,height):

	for j in range (0,width):

		te = ""
		pixel = image[i,j]
		#print pixel

		pixel2 = dec_to_bin(pixel[0])

		te+=pixel2[6]
		te+=pixel2[7]

		pixel1 = dec_to_bin(pixel[1])
		te+=pixel1[5]
		te+=pixel1[6]
		te+=pixel1[7]

		pixel0 = dec_to_bin(pixel[2])
		te+=pixel0[5]
		te+=pixel0[6]
		te+=pixel0[7]

		tem=chr(int(te,2))
		if ord(tem)==ord('!'):
			tte=1
			break
		ans+=chr(int(te,2))
		k=k+1
	if tte==1:
		break

print ans