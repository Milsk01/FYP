import os

path = r'output\rec'

model = {
    'predicts_abinet.txt':'ABINet', 
    'predicts_b3_rare_r34_none_gru.txt':'RARE', 
    'predicts_r32_gaspin_bilstm_att.txt':'SPIN', 
    'predicts_r34_vd_none_bilstm_ctc.txt':'CRNN',
    'predicts_r34_vd_none_none_ctc.txt':'Rosetta', 
    'predicts_r34_vd_tps_bilstm_ctc.txt':'STAR-Net', 
    'predicts_robustscanner.txt':'RobustScanner', 
    'predicts_srn.txt':'SRN', 
    'predicts_svtr_tiny.txt':'SVTR', 
    'predicts_visionlan.txt':'VisionLAN', 
    'predicts_vitstr.txt':'ViTSTR', 
    'rec_resnet_rfl.txt':'RFL'
}


for file in os.listdir(path):
    if file.endswith('.txt'):
        with open(os.path.join(path,file),'r') as f:
            Lines = f.readlines()
            with open(os.path.join(path,model[file])+'.txt','a') as new_file:

                for L in Lines :
                    filename,text,confidence = L.split('\t')

                    # split file into name and extension
                    name, ext = os.path.splitext(filename)

                    # split name into words by \
                    words = name.split('\\')

                    cols = words[1].split('-')

                    # format file name into word_ooo.png
                    filename = 'word_'+ cols[0]+'.png'

                    # from text remove all -, : ,.
                    text = text.replace('-','')
                    text = text.replace(':','')
                    text = text.replace('.','')

                    # line format : word_ooo.png,"text" 
                    new_file.write(filename+',"'+text+'"'+'\n')



