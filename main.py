from PIL import Image
import numpy as np
import cv2
import pytesseract
import argparse
from urllib.request import urlopen

parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument('--path', type=str)
parser.add_argument('--url', type=str)

# Parse the argument
args = parser.parse_args()

if args.url is None and args.path is None:
   pa.error("at least one of --path and --url required")

else:
    # Change this path if you install pytesseract in another folder:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    if args.path:
        img = np.array(Image.open(args.path))
    else:
        img = np.array(Image.open(urlopen(args.url)))

    custom_config = r"--oem 3 --psm 11 -c tessedit_char_whitelist= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '"

    # Image Preprocessings
    def preprocess_final(im):
        im= cv2.bilateralFilter(im,5, 55,60)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        _, im = cv2.threshold(im, 240, 255, 1)
        return im

    img=preprocess_final(img)
    text = pytesseract.image_to_string(img, lang='eng', config=custom_config)

    print('-'*40)
    print("Meme Content: \n\n",text.replace('\n', ''))
    print('-'*40)
