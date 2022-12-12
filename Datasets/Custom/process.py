import os 
import shutil

SRC_DIR= 'Dataset'
CONDITIONS = ['Rotated','Blurry','Blur','Ideal','Glare','Rotate']
CONDITIONS = [CONDITIONS.lower() for CONDITIONS in CONDITIONS]

import os 

def rename(path):
    # for every folder in Output 
    for folder in os.listdir(path):
        # define a counter 
        counter = 0

        # for every file in the folder
        for file in os.listdir(os.path.join(path,folder)):
            # separate the name and the file extension
            name, ext = os.path.splitext(file)

            # rename the file to image + _ + counter + file extension
            os.rename(os.path.join(path,folder,file),os.path.join(path,folder,'image_'+str(counter)+ext))

            counter += 1


def get_file_name(path):
    return os.path.basename(path)


def get_file_extension(path):
    return os.path.splitext(path)[1]

def copy_files(src, dest):
    for file in os.listdir(src):
        src_file = os.path.join(src, file)
        dest_file = os.path.join(dest, file)
        shutil.copy(src_file, dest_file)

def delete_files(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        os.remove(file_path)

def delete_folder(path):
    delete_files(path)
    shutil.rmtree(path)


def rename_files(path, new_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        new_file_path = os.path.join(path, new_name + get_file_extension(file))
        os.rename(file_path, new_file_path)

def rename_folder(path, new_name):
    new_path = os.path.join(os.path.dirname(path), new_name)
    os.rename(path, new_path)

def get_file_list(path):
    return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

def get_folder_list(path):
    return [file for file in os.listdir(path) if os.path.isdir(os.path.join(path, file))]

def main():
    # create a folder for the output
    if 'Output' not in os.listdir():
        os.mkdir('Output')
    
    # extract the list of folder names
    folder_list = get_folder_list(SRC_DIR)

    # create a folder for each condition
    for condition in CONDITIONS:
        if condition not in os.listdir('Output'):
            os.mkdir(os.path.join('Output',condition))

    # output the result to another folder
    for folder in folder_list:
        src_folder = os.path.join(SRC_DIR,folder)
        dest_folder = os.path.join('Output',folder)

        # for every condition
        for condition in CONDITIONS:
            for file in os.listdir(src_folder):
                # if the condition is in the file name
                if condition in file.lower():
                    # copy the file to the corresponding folder
                    dest = os.path.join('Output',condition)
                    src = os.path.join(src_folder,file)
                    shutil.copy(src, dest)
        
    # copy files from blur to blurry, rotated to rotate
    copy_files(os.path.join('Output','blur'), os.path.join('Output','blurry'))
    copy_files(os.path.join('Output','rotated'), os.path.join('Output','rotate'))


    # remove files from blur and rotated
    delete_files(os.path.join('Output','blur'))
    delete_files(os.path.join('Output','rotated'))

    # delete blur folder
    delete_folder(os.path.join('Output','blur'))
    delete_folder(os.path.join('Output','rotated'))

    rename('Output')


main()




