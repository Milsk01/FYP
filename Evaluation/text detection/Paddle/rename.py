import os
from ast import literal_eval



for model in os.listdir():
    # if is a directory
    if os.path.isdir(model):
        for text_file in os.listdir(model):
            if text_file == 'det_results.txt' and model == 'PSE':
                print(model,text_file)

                with open(os.path.join(model,text_file), 'r') as f:
                    lines = f.readlines()
                    for idx,line in enumerate(lines):

                        name, bboxes = line.split('\t')
                        print(idx,name)

                        mainlist = list(literal_eval(bboxes))

                        # filename = 'res_' + text_file
                        filename = 'res_' + name.split('.')[0] + '.txt'
                        
                        with open(os.path.join(model,filename), 'w') as f:
                            for bbox in mainlist:
                                result = ''
                                for coordinates in bbox:
                                    for coordinate in coordinates:
                                        result += str(int(coordinate))+ ','
                                result =result[:-1] +'\n'
                                f.write(result)
                                    
                    


