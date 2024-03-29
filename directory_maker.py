import os

target_directory="Data/Original"
FileName=['1','2','3','4','5','6','7','8','9','0']
for i in FileName:
    target=target_directory+'/'+i
    if not os.path.exists(target):
        os.makedirs(target)
    else:
        print(f'Directory {target} is already exists')
print("Making directory is done")
