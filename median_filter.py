import cv2 as cv
import sys
import math

window_size = 3
img = cv.imread("az.png")
padded_img = cv.copyMakeBorder(img, 1, 1, 1, 1, cv.BORDER_REPLICATE, value=0)


center_start = (window_size - 1)/2

#iterates for each pixel
for i in range(padded_img.shape[0] - window_size):
    for j in range(padded_img.shape[1] - window_size):

        window = []
        #getting the values in the window
        for l in range(window_size):
            for k in range(window_size):
                window.append(padded_img[l+i][k+j][0])
        #sort the values
        window.sort()
        #get the median
        median_value = window[math.ceil((pow(window_size, 2)-1)/2)]
        #replace the pixel with its median value
        padded_img[i+1][j+1] = median_value

        #for demonstration purposes only
        #cv.imshow("live preview", padded_img)
        #cv.waitKey(1)


cv.imshow("sdfsd", padded_img)
cv.waitKey(0)

print(img)