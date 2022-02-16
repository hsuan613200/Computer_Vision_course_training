import cv2
import numpy as np
import matplotlib.pyplot as plt

image = "lena.bmp"
img = cv2.imread(image)

# cv2.imshow("lena", img)

#1.a binary image (threshold at 128)
binary = np.array(img)

binary[img >= 128] = 255
binary[img < 128] = 0
binary = binary.astype('uint8')
cv2.imshow("binary", binary)


#2.a histogram
histogram = np.zeros(255)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        histogram[img[x][y]] += 1
        
plt.bar(range(0, 255), histogram)
plt.show()

#3.connected components(regions with + at centroid, bounding box)



# cv2.waitKey(0)