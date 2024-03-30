# This program is used to loop all the images in the folder

# import functions
import image_crop
import file_checker

# destinations
sourceDest='Data/Original'
targetDest='Data/Processed'

# data to be processed
numbers=['1','0','2','3','4','5','6','7','8','9']
lux=['4000LUX']
distance=['10cm','15cm','20cm','25cm','30cm','35cm','40cm']
degree=['+45deg','+30deg','+15deg','0deg','-15deg','-30deg','-45deg']

# data not to be processed
dataList=['1/4000LUX_20cm_-15deg.png',
          '1/4000LUX_25cm_-15deg.png',
          '1/4000LUX_30cm_+45deg.png',
          '1/4000LUX_30cm_-30deg.png',
          '1/4000LUX_35cm_+30deg.png',
          '1/4000LUX_35cm_-30deg.png',
          '1/4000LUX_40cm_-30deg.png',
          '0/4000LUX_10cm_-45deg.png',
          '0/4000LUX_25cm_-15deg.png',
          '0/4000LUX_35cm_-15deg.png',
          '2/4000LUX_15cm_+45deg.png',
          '2/4000LUX_30cm_+30deg.png',
          '3/4000LUX_10cm_+30deg.png',
          '3/4000LUX_25cm_-30deg.png'
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
        for j in lux:
            for k in distance:
                for l in degree:
                    source=sourceDest+'/'+i+'/'+j+'_'+k+'_'+l+'.png'
                    target=targetDest+'/'+i+'/'+j+'_'+k+'_'+l+'.png'
                    if source not in dataList:
                        #image_crop.process_image(source,target)
                        file_checker.file_check(target)
