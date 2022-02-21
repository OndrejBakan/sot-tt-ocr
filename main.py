import cv2 as cv
import numpy as np
import os

img = cv.imread('8_story_denik.png', -1)
#img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#img = cv.GaussianBlur(img, (5, 5), 0)
#ret, th = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)


for file in os.listdir('./runes'):
    if file == 'From_i.png':
        template = cv.imread(os.path.join('./runes', file), -1)
        #template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
        template = cv.resize(template, (86, int(86 / 1.0141987829614604462474645030426)))
        
        res = cv.matchTemplate(img, template, cv.TM_CCOEFF, None, template)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + 86, top_left[1] + 84)
        cv.rectangle(img, top_left, bottom_right, 255, 2)

    #cv.imshow('template', template)

# output
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()