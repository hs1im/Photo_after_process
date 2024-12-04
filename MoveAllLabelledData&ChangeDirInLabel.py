import os
import tqdm
import shutil
import xml.etree.ElementTree as ET

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

# Make directories of val and test
os.makedirs(targetDir + "/train", exist_ok=True)
os.makedirs(targetDir + "/val", exist_ok=True)


# Make directories of images and labels
os.makedirs(targetDir + "/train/images", exist_ok=True)
os.makedirs(targetDir + "/train/labels", exist_ok=True)
os.makedirs(targetDir + "/val/images", exist_ok=True)
os.makedirs(targetDir + "/val/labels", exist_ok=True)

# Rotate the all files in the directory
numbers = [str(i) for i in range(10)]
dir = ['val','train']
for dir_idx in dir:
    for num_idx in tqdm.tqdm(numbers):
        # Get all files
        fileList = os.listdir(sourceDir+"/"+dir_idx+"/"+num_idx)

        # Process each file
        for filename in fileList:
            # Check the Label file extension
            fileType = filename.split(".")[1]
            if(fileType != "xml"):
                continue

            # File which has label
                # Copy image
            filename = filename.split(".")[0]
            sourceFile = sourceDir+"/"+dir_idx+"/"+num_idx+"/"+filename+".png"
            targetFile = targetDir+"/"+dir_idx+"/images"+"/"+num_idx+"_"+filename+".png"
            shutil.copy(sourceFile, targetFile)
                # Copy label
            sourceFile = sourceDir+"/"+dir_idx+"/"+num_idx+"/"+filename+".xml"
            targetFile = targetDir+"/"+dir_idx+"/labels"+"/"+num_idx+"_"+filename+".xml"
            shutil.copy(sourceFile, targetFile)
                # Edit label
            tree = ET.parse(targetFile)
            root = tree.getroot()
            filePath = "Data"+"/"+dir_idx+"/images"+"/"+num_idx+"_"+filename+".png"

            pathTag = root.find('path')
            if(pathTag is not None):
                pathTag.text = filePath
            
            tree.write(targetFile)


            