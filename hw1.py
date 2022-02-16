from PIL import Image
import cv2
import numpy as np

image = "lena.bmp"
img_cv = cv2.imread(image)

cv2.imshow("lena", img_cv)

#1.upside-down lena.im
reverse_idx = np.arange(511,-1,-1)
upside_down = np.zeros(img_cv.shape)
upside_down[reverse_idx] = img_cv[:]
upside_down = upside_down.astype('uint8')

# cv2.imshow("up_down", upside_down)

#2.right-side-left lena.bmp
reverse_idx = np.arange(511,-1,-1)
right_side_left = np.zeros(img_cv.shape)
right_side_left[:,reverse_idx] = img_cv[:,:]
right_side_left = right_side_left.astype('uint8')

# cv2.imshow("right_left", right_side_left)

#3.diagonally flip lena.bmp
diagonally_flip = np.zeros(img_cv.shape)
for i in range(img_cv.shape[0]):
    for j in range(img_cv.shape[1]):
        diagonally_flip[i][j] = img_cv[j][i]
diagonally_flip = diagonally_flip.astype('uint8')

# cv2.imshow("diagonally_flip", diagonally_flip)


cv2.waitKey(0)