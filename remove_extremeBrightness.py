import os
import shutil
import tqdm

Start = "Data/Original/train"
Destination = "Data/Processed/train"
FileName=['1','2','3','4','5','6','7','8','9','0']
for num_i in tqdm.tqdm(FileName):
    target=Destination+'/'+num_i
    source=Start+'/'+num_i
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = os.path.join(root, file)
            fileNames = file.split(".")[0]
            brightness=fileNames.split("_")[2]
            if brightness == "brighter2" or brightness == "darker2":
                continue
            shutil.copy(file_path, target)