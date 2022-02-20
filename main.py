import cv2
import numpy as np
import os


img = cv2.imread('8_story_denik.png', 0)
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img, 50, 100)

templates = []
templates_shapes = []

template = cv2.imread('runes/From.jpg', 0)
#template = cv2.cvtColor(template, cv2.COLOR_RGBA2mRGBA)
#template = cv2.cvtColor()
template_resized = cv2.resize(template, (105, int( 105 / 1.0141987829614604462474645030426)))
template_canny = cv2.Canny(template_resized, 50, 100)
cv2.imshow('template', template_canny)
#rune_gray = cv2.cvtColor(rune_canny, cv2.COLOR_BGR2GRAY)
h, w = template_resized.shape

# template matching
print('Matching...')

# res = cv2.matchTemplate(img_canny, rune_canny, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

#result = cv2.matchTemplate(img, template_resized, cv2.TM_CCOEFF)
#loc = np.where(result >= 0.95)

#for pt in zip(*loc[::-1]):
#    cv2.rectangle(img, pt, (pt[0] + 86, pt[1] + 84), (0,255,0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()