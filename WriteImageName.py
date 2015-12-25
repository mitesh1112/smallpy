#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MITESH
#
# Created:     25-12-2015
# Copyright:   (c) MITESH 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import PIL
import PIL.Image
import PIL.ImageDraw

def process():
    image_source_path = 'D:\\mitesh\\Pics\\'
    image_target_path =  'D:\\mitesh\\Pics\\t\\'

    i = 1
    # Get all image files
    image_files = [f for f in os.listdir(image_source_path) if os.path.splitext(f)[1] == '.jpg' ]
    for fn in image_files:
        fp = image_source_path + fn
        img = PIL.Image.open(fp)
        draw = PIL.ImageDraw.Draw(img)

        if img.width > img.height:
            # Landscape

            x = img.width / 2
            y = img.height - 20
        else:
            # Portrait

            x = img.height / 2
            y = img.width - 20


        draw.text((x, y), 'File ' + str(i))
        img.save(image_target_path + fn)
        i = i + 1

        print('File Name: {0} - {1} X {2}'.format(fn, img.width, img.height))


def main():
    process()

if __name__ == '__main__':
    main()
