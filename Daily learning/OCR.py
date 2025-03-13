"OCR experiments"

import pytesseract
from pytesseract import Output
import PIL.Image
import cv2

"""

Page segmentation modes: 
O Orientation and script detection (OSD) only
1 Automatic page segmentation with OSD.
2 Automatic page segmentation, but no OSD, or OCR.
3 Fully automatic page segmentation, but no OSD. (Default)
4 Assume a single column of text of variable sizes.
5 Assume a single uniform block of vertically aligned text.
6 Assume a single uniform block of text
7 Treat the image as a single text line.
8 Treat the image as a single word.
9 Treat the image as a single word in a circle.
10 Treat the image as a single character.
11 Sparse text. Find as much text as possible in no particular order.
12 Sparse text with OSD.
13 Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract—specific.

"""


myconfig = "--psm 3 --oem 3"

# text = pytesseract.image_to_string("E:\Desktop\Screens\Human In the loop\Interview.png", config=myconfig)
# print(text)
img = cv2.imread("E:\\Desktop\\Screens\\Human In the loop\\Interview.png")
height, width, _ = img.shape

boxes = pytesseract.image_to_boxes(img, config=myconfig)
for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 0, 255), 1)

cv2.imshow("image", img)
cv2.waitKey(0)

# data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

# amount = len(data["text"])
# for i in range(amount):
#     if float(data["conf"][i]) > 90:
#         (x, y, width, height) = (data["left"][i], data["top"][i], data["width"][i], data["height"][i])
#         img = cv2.rectangle(img, (x, y), (x+width, y+height), (0, 0, 255), 1)

# cv2.imshow("img", img)
# cv2.waitKey(0)