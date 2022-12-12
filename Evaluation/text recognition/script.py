import os
import sys

from  edit_distance import eval
GT_DIGITS_WITH_SPECIAL_CHAR = 'ground_truth/Web/gt.txt'
GT_DIGITS_ONLY = 'ground_truth/Web/gt_digits_only.txt'

# create output folder
if not os.path.exists('output'):
    os.makedirs('output')

projects = ['mmocr','paddle','parseq']
# create project folder in output 
for p in projects:
    if not os.path.exists(os.path.join('output',p)):
        os.makedirs(os.path.join('output',p))

# mmocr model can only detect characters and numbers
# create digits_only folder in mmocr project folder
if not os.path.exists(os.path.join('output','mmocr','digits_only')):
    os.makedirs(os.path.join('output','mmocr','digits_only'))

# for predicted in os.listdir('mmocr'):
#     if predicted.endswith('.txt'):
#         eval(os.path.join('mmocr',predicted),GT_DIGITS_ONLY,os.path.join('Output','mmocr','digits_only',predicted.split('.')[0]))
        
# for predicted in os.listdir('paddle/Converted'):
#     if predicted.endswith('.txt'):
#         eval(os.path.join('paddle/Converted',predicted),GT_DIGITS_ONLY,os.path.join('Output','paddle','digits_only',predicted.split('.')[0]))


# make a digits_only folder in parseq project folder
if not os.path.exists(os.path.join('output','parseq','digits_only')):
    os.makedirs(os.path.join('output','parseq','digits_only'))


# # make a digits_with_special_char folder in parseq project folder
# if not os.path.exists(os.path.join('output','parseq','digits_with_special_char')):
#     os.makedirs(os.path.join('output','parseq','digits_with_special_char'))

print('\n\n')
for file in os.listdir(os.path.join('parseq/Web','digits_only')):
    input_path = os.path.join('parseq/Web','digits_only',file)
    eval(input_path,GT_DIGITS_ONLY,os.path.join('Output','parseq','digits_only',file.split('.')[0]))

print('\n\n')
for file in os.listdir(os.path.join('parseq/Web','digits_with_special_char')):
    input_path = os.path.join('parseq/Web','digits_with_special_char',file)
    eval(input_path,GT_DIGITS_ONLY,os.path.join('Output','parseq','digits_with_special_char',file.split('.')[0]))
