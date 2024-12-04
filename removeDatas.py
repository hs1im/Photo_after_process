import tqdm
import shutil
import os

# Directory paths
sourceDir = 'Data/Splitted'
targetDir = 'Data/forTrain'

# Remain Data
dir = ['val','train']
numbers = [str(i) for i in range(10)]
distance=["5cm","10cm","15cm","20cm","25cm"]
angel=["-50deg","-40deg","-30deg","-20deg","-10deg","0deg","+10deg","+20deg","+30deg","+40deg","+50deg"]
brighter=["LOW","MID","HIGH"]

for dir_idx in dir:
    for number_idx in tqdm.tqdm(numbers):
        fileList = os.listdir(sourceDir+"/"+dir_idx+"/"+number_idx)
        for filename in fileList:
            filename = filename.split(".")[0]
            fileElement = filename.split("_")
            if(fileElement[0] in distance and fileElement[1] in angel and fileElement[2] in brighter):
                sourceFile = sourceDir+"/"+dir_idx+"/"+number_idx+"/"+filename+".png"
                targetFile = targetDir+"/"+dir_idx+"/"+number_idx+"/"+filename+".png"
                shutil.copyfile(sourceFile, targetFile)
