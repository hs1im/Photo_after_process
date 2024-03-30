# This program is used to loop all the images in the folder

# import functions
import image_crop

# destinations
sourceDest='Data/Original'
targetDest='Data/Processed'

# data to be processed
numbers=['1','0','2','3','4','5','6','7','8','9']
lux=['4000LUX']
distance=['10cm','15cm','20cm','25cm','30cm','35cm','40cm']
degree=['+45deg','+30deg','+15deg','0deg','-15deg','-30deg','-45deg']

# bookmark


# loop
for i in numbers:
    for j in lux:
        for k in distance:
            for l in degree:
                source=sourceDest+'/'+i+'/'+j+'_'+k+'_'+l+'.png'
                target=targetDest+'/'+i+'/'+j+'_'+k+'_'+l+'.png'
                image_crop.process_image(source,target)