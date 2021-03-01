import argparse
from Image_2_Text import i2t
from Text_2_Speech import t2s

ap=argparse.ArgumentParser()
ap.add_argument("--image", "-i", required=True, help="Image Location")
arguments=vars(ap.parse_args())

text = i2t(arguments['image'])

print(text)

t2s(text)