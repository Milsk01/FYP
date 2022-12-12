import os 


# for every folder in Output 
for folder in os.listdir('Output'):
    # define a counter 
    counter = 0

    # for every file in the folder
    for file in os.listdir(os.path.join('Output',folder)):
        # separate the name and the file extension
        name, ext = os.path.splitext(file)

        # rename the file to image + _ + counter + file extension
        os.rename(os.path.join('Output',folder,file),os.path.join('Output',folder,'image_'+str(counter)+ext))

        counter += 1



