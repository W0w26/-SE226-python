import cv2

image = cv2.imread('image.jpg')

b, g, r = cv2.split(image)

cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)
cv2.waitKey(0)

g[:] = 0

image = cv2.merge((b, g, r))

cv2.imshow('Modified Image', image)
cv2.waitKey(0)