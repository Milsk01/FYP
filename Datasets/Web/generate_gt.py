import os

path = 'images'
with open("gt_digits_only.txt", "w") as f:
    for file in os.listdir(path):
        number ,text = file.split('-')

        # convert the image to png
        text, extension = text.split('.')

        filename = 'word'+'_'+number+'.'+extension

        f.write(filename+','+'\"'+text +'\"'+'\n')

        # rename the files to word_number + file extension
        os.rename(os.path.join(path,file),os.path.join(path,filename))