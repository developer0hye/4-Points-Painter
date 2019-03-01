import openpyxl
import argparse
import os
import cv2

parser = argparse.ArgumentParser(description='Image 4 points painting Helper')

parser.add_argument('--xl', metavar='DIR', help='path to xl_file')
parser.add_argument('-i', '--img_path', metavar='DIR', help='path to input images')
parser.add_argument('-o', '--output_img_path', metavar='DIR', help='path to output images')

args = parser.parse_args()

# read the excel file
xl = openpyxl.load_workbook(args.xl, read_only=True)
xl_a = xl.active

if not(os.path.isdir(args.output_img_path)):
        os.makedirs(args.output_img_path)
        
color_table = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)]

for row in xl_a.rows:

    img_name = row[0].value
    img_full_path = os.path.join(args.img_path, img_name)
    print("image full path:", img_full_path)

    # open the image
    img = cv2.imread(img_full_path)

    if img is not None:
        img_draw = img.copy()

        # get 4 points
        for i in range(0, 4):
            point = (row[i * 2 + 1].value, row[i * 2 + 2].value)
            cv2.circle(img_draw, point, 5, color_table[i], -1)

        cv2.imshow("img", img)
        cv2.imshow("img_draw", img_draw)

        cv2.imwrite(os.path.join(args.output_img_path, img_name), img_draw)

        cv2.waitKey(1000)







xl.close()

