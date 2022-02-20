import cv2
import os
import numpy as np
import imutils


templates = []
templates_shapes = []
threshold = 0.5

# load templates
for file in os.listdir('./runes'):
    # load template
    template = cv2.imread(os.path.join('./runes', file))

    # resize template
    (h, w) = template.shape[:2]
    dimensions = (64, int(h * 64 / float(w)))
    template = cv2.resize(template, dimensions, cv2.INTER_AREA)

    # further edit
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)

    templates.append(template)
    templates_shapes.append(template.shape[::-1])

# loop / scale
img = cv2.imread('8_story_denik.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
found = None


for template in templates:
    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        resized = imutils.resize(img, width = int(img.shape[1] * scale))
        r = img.shape[1] / float(resized.shape[1])

        # if the resized image is smaller than the template, then break
	    # from the loop
        if resized.shape[0] < 128 or resized.shape[1] < 128:
            break

        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)
    
    (_, maxLoc, r) = found
    (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
    (endX, endY) = (int((maxLoc[0] + 128) * r), int((maxLoc[1] + 128) * r))

    cv2.rectangle(img, (startX, startY), (endX, endY), (0, 0, 255), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# rune = cv2.imread('runes/From.png', cv2.IMREAD_UNCHANGED)
# rune_gray = cv2.cvtColor(rune, cv2.COLOR_RGBA2mRGBA)
# #rune_gray = cv2.cvtColor(rune, cv2.COLOR_BGR2GRAY)
# rune_resized = cv2.resize(rune_gray, (86, int(86 / 1.0141987829614604462474645030426)))
# rune_canny = cv2.Canny(rune_resized, 50, 100)
# #rune_gray = cv2.cvtColor(rune_canny, cv2.COLOR_BGR2GRAY)
# h, w,_ = rune_resized.shape

# print(rune_resized.dtype)

# cv2.imshow('rune', rune_canny)

# res = cv2.matchTemplate(img_canny, rune_canny, cv2.TM_CCOEFF)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)