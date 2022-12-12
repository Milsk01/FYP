import os


# for text_file in os.listdir():
#     if text_file.endswith('.txt'):
#         new_name = 'res_' + text_file
#         os.rename(text_file, new_name)

# delete the last csv values 
for text_file in os.listdir():
    if text_file.endswith('.txt'):
        lines = []
        with open(text_file, 'r') as f:
            lines = f.readlines()

            lines = [line.split(',') for line in lines]
            
        if len(lines) > 0:
            with open(text_file, 'w') as f:
                for line in lines:
                    line = line[:-1]
                    print(len(lines))
                #write 8 coordinates of the bounding box to the file
                    f.write(str(line[0]) + "," + str(line[1]) + "," + str(line[2]) + "," + str(line[3]) + "," + str(line[4]) + "," + str(line[5]) + "," + str(line[6]) + "," + str(line[7]) + "\n")

        else:
            continue
