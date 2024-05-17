# This program is used to loop all the images in the folder

# import functions
import image_crop
import file_checker
import photo_brightness_change
import image_sizeGet
import keyboard
import time

# destinations
sourceDest='Data/Original'
targetDest='Data/Processed'

# data to be processed
numbers=['0','1','2','3','4','5','6','7','8','9']
lux=['4000LUX']
distance=['10cm','15cm','20cm','25cm','30cm']
degree=['+45deg','+30deg','+15deg','0deg','-15deg','-30deg','-45deg']

# data not to be processed
dataList=[
    '0/20cm_-45deg.png',
    '0/20cm_+45deg.png'
    ]

# switch of loop going not processed data
dataNotProcessedSW=False


# loop
if dataNotProcessedSW:
    for i in dataList:
        source=sourceDest+'/'+i
        target=targetDest+'/'+i
        image_crop.process_image(source,target)
else:
    for i in numbers:
        #for j in lux:
        for k in distance:
            print(f'number:{i} {k}')
            for l in degree:
                source=sourceDest+'/'+i+'/'+k+'_'+l+'.png'
                target=targetDest+'/'+i+'/'+k+'_'+l
                #image_crop.process_image(source,target)
                #file_checker.file_check(target)
                    #image_sizeGet.image_size_get_size(target,1)
                photo_brightness_change.photo_brightness_change(source,target,True,2,2)
