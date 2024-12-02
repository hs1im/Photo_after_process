import random
import os
import shutil
import tqdm
import photo_brightness_change

# Directory paths
sourceDir = 'Data/Original'
targetDir = 'Data/Processed'

# Iterate over all the files and directories in the specified directory
for root, dirs, files in os.walk(targetDir, topdown=False):
    for file in files:
        # Remove files
        os.remove(os.path.join(root, file))
    for dir in dirs:
        # Remove directories
        os.rmdir(os.path.join(root, dir))

# Split the array into three parts
distance=["0cm","10cm","20cm","30cm","40cm","50cm","60cm","70cm","80cm","90cm","100cm","110cm","120cm","130cm","140cm","150cm","160cm","170cm","180cm"]
angel=["-90deg","-80deg","-70deg","-60deg","-50deg","-40deg","-30deg","-20deg","-10deg","0deg","+10deg","+20deg","+30deg","+40deg","+50deg","+60deg","+70deg","+80deg","+90deg"]
for i in tqdm.tqdm(range(10)):
    os.makedirs(targetDir+"/"+str(i), exist_ok=True)
    for distance_idx in distance:
        for angel_idx in angel:
            os.makedirs(targetDir+"/"+str(i)+"/"+distance_idx+"_"+angel_idx, exist_ok=True)
            shutil.copy(sourceDir+"/original/"+str(i)+"/"+distance_idx+"_"+angel_idx+".png", targetDir+"/"+str(i)+"/"+distance_idx+"_"+angel_idx+"/Original.png")
            shutil.copy(sourceDir+"/Sliced/"+str(i)+"/"+distance_idx+"_"+angel_idx+".png", targetDir+"/"+str(i)+"/"+distance_idx+"_"+angel_idx+"/Sliced.png")
            os.makedirs(targetDir+"/"+str(i)+"/"+distance_idx+"_"+angel_idx+"/Bright", exist_ok=True)
            photo_brightness_change.photo_brightness_change(sourceDir+"/Sliced/"+str(i)+"/"+distance_idx+"_"+angel_idx+".png",targetDir+"/"+str(i)+"/"+distance_idx+"_"+angel_idx+"/Bright/",True,2,2)