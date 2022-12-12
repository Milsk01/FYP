import os 
import cv2
import pandas as pd

def crop():
    # create output folder if not exist
    if not os.path.exists('Output'):
        os.makedirs('Output')
    # remove all files in output folder
    for file in os.listdir('Output/'):
        os.remove('Output/'+file)

    # load images from Testing

    for image in os.listdir('Testing/'):
        img = cv2.imread('Testing/'+image)
        
        # crop image from right 10 ccm 
        img = img[:, :-100]

        # save image
        cv2.imwrite('Output/'+image, img)


def rename():
    # rename every fle in Testing folder 

    # name format
    # gt_img_###.jpg
    for image in os.listdir('Output/'):

        # get the number of the image in the paranthesis
        number = image.split('(')[1].split(')')[0]

        # rename the image
        os.rename('Output/'+image, 'Output/img_'+str(number)+'.jpg')

def generate_gt():
    labels = pd.read_pickle(r'label.pickle')

    # create gt folder if not exist
    if not os.path.exists('gt'):
        os.makedirs('gt')
        
    for label in labels:
        number = label[0].split('(')[1].split(')')[0]
        with open('gt/gt_img_'+str(number)+'.txt', 'w') as f:

            label_1 = str(label[2]) + str(label[4]) + str(label[6]) + str(label[8])
            label_2 = str(label[10]) + str(label[12]) + str(label[14]) + str(label[16])

            box_1 = [label[1], label[3], label[5], label[7]]
            top_left_1 = (box_1[0][0], box_1[0][1])
            bottom_right_1 = (box_1[3][2], box_1[3][3])
            h_1 = bottom_right_1[1] - top_left_1[1]
            w_1 = bottom_right_1[0] - top_left_1[0]
            top_right_1 = (top_left_1[0] + w_1, top_left_1[1])
            bottom_left_1 = (top_left_1[0], top_left_1[1] + h_1)

            #plot the four corner 

            box_2 = [label[9], label[11], label[13], label[15]]
            top_left_2 = (box_2[0][0], box_2[0][1])
            bottom_right_2 = (box_2[3][2], box_2[3][3])
            h_2 = bottom_right_2[1] - top_left_2[1]
            w_2 = bottom_right_2[0] - top_left_2[0]
            top_right_2 = (top_left_2[0] + w_2, top_left_2[1])
            bottom_left_2 = (top_left_2[0], top_left_2[1] + h_2)

            # write the four coordinate into the text file 
            f.write(str(top_left_1[0]) + ',' + str(top_left_1[1]) + ',' + str(top_right_1[0]) + ',' + str(top_right_1[1]) + ',' + str(bottom_right_1[0]) + ',' + str(bottom_right_1[1]) + ',' + str(bottom_left_1[0]) + ',' + str(bottom_left_1[1]) + ','+label_1+'\n')
            f.write(str(top_left_2[0]) + ',' + str(top_left_2[1]) + ',' + str(top_right_2[0]) + ',' + str(top_right_2[1]) + ',' + str(bottom_right_2[0]) + ',' + str(bottom_right_2[1]) + ',' + str(bottom_left_2[0]) + ',' + str(bottom_left_2[1]) +','+ label_2)
    

if __name__ == '__main__':
    crop()
    rename()
    generate_gt()