import random
import os
import shutil
import tqdm

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
os.makedirs(targetDir + "/val", exist_ok=True)
os.makedirs(targetDir + "/test", exist_ok=True)
os.makedirs(targetDir + "/train", exist_ok=True)
for i in range(10):
    os.makedirs(targetDir + "/val/" + str(i), exist_ok=True)
    os.makedirs(targetDir + "/test/" + str(i), exist_ok=True)
    os.makedirs(targetDir + "/train/" + str(i), exist_ok=True)

# Array size and number of each digit
size = 1805
num_each_digit = size // 10 + 1

# Generate two arrays
digits = [i for i in range(10)] * num_each_digit
val_array = random.sample(digits, size)
test_array = random.sample(digits, size)

# Check same number in the same index
for i in range(size):
    if val_array[i] == test_array[i]:
        changeSw=True
        # Find a different number in the same index
        for j in range(i + 1, size):
            if test_array[j] != val_array[i] and test_array[j] != val_array[j]:
                test_array[i], test_array[j] = test_array[j], test_array[i]
                changeSw=False
                break
        if changeSw:
        # Can't find replace number in the array
            for j in range(0, i):
                if test_array[j] != val_array[i] and test_array[j] != val_array[j]:
                    test_array[i], test_array[j] = test_array[j], test_array[i]
                    changeSw=False
                    break
        if changeSw:
            print("Can't find replace number in the array")
            exit(0)

# Split the array into three parts
distance=["0cm","10cm","20cm","30cm","40cm","50cm","60cm","70cm","80cm","90cm","100cm","110cm","120cm","130cm","140cm","150cm","160cm","170cm","180cm"]
angel=["-90deg","-80deg","-70deg","-60deg","-50deg","-40deg","-30deg","-20deg","-10deg","0deg","+10deg","+20deg","+30deg","+40deg","+50deg","+60deg","+70deg","+80deg","+90deg"]
brighter=["brighter1","brighter2","original","darker1","darker2"]

# split the array into three parts
idx=0
for distance_idx in tqdm.tqdm(distance):
    for angel_idx in angel:
        for brighter_idx in brighter:
            if idx<size:
                # shutil Val data
                sourceFile = sourceDir + "/" + str(val_array[idx]) + "/" + distance_idx + "_" + angel_idx + "_" + brighter_idx + ".png"
                targetFile = targetDir + "/val/" + str(val_array[idx]) + "/" + distance_idx + "_" + angel_idx + "_" + brighter_idx + ".png"
                shutil.copy(sourceFile, targetFile)

                # shutil Test data
                sourceFile = sourceDir + "/" + str(test_array[idx]) + "/" + distance_idx + "_" + angel_idx + "_" + brighter_idx + ".png"
                targetFile = targetDir + "/test/" + str(test_array[idx]) + "/" + distance_idx + "_" + angel_idx + "_" + brighter_idx + ".png"
                shutil.copy(sourceFile, targetFile)

                # Shutil Train data
                for i in range(10):
                    if i != val_array[idx] and i != test_array[idx]:
                        sourceFile = sourceDir + "/" + str(i) + "/" + distance_idx + "_" + angel_idx + "_" + brighter_idx + ".png"
                        targetFile = targetDir + "/train/" + str(i) + "/" + distance_idx + "_" + angel_idx + "_" + brighter_idx + ".png"
                        shutil.copy(sourceFile, targetFile)

                idx+=1
            else:
                print("Error: The number of images is not enough.")
                break

# Well done
print("Finish with no problem.")