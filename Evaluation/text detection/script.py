import os
import sys

from  iou import eval
GT_PATH = 'gt.zip' 

# create output folder
if not os.path.exists('output'):
    os.makedirs('output')

projects = ['CharNet','MMOCR','Paddle','TextFuseNet']

# create project folder in output
for p in projects:
    if not os.path.exists(os.path.join('output',p)):
        os.makedirs(os.path.join('output',p))


# charnet textfusenet 
eval('CharNet/results.zip',GT_PATH,os.path.join('output','CharNet'))

# eval('TextFuseNet/results.zip',GT_PATH,os.path.join('output'))

# for model in os.listdir('Paddle'):
#     # if is a directory
#     if os.path.isdir(os.path.join('Paddle',model)):
#         if model == 'EAST':
#             continue

#         #create model folder in output
#         if not os.path.exists(os.path.join('output','Paddle',model)):
#             os.makedirs(os.path.join('output','Paddle',model))
#         if os.path.isdir(os.path.join('Paddle',model)):
#             eval(os.path.join('Paddle',model,'results.zip'),GT_PATH,os.path.join('output','Paddle',model))


mmocr_models = [
    "DB_r18",
    "DB_r50",
    "DBPP_r50",
    "MaskRCNN_IC15",
    "MaskRCNN_IC17",
    "PANet_IC15",
    "PS_IC15"]


# for model in mmocr_models:
#     print(model)
#     if not os.path.exists(os.path.join('output','mmocr',model)):
#             os.makedirs(os.path.join('output','mmocr',model))
            
#     eval(os.path.join('mmocr',model,'results.zip'),GT_PATH,os.path.join('output','mmocr',model))