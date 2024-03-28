import sys
sys.path.append('c:/users/49228/anaconda3/envs/tactile_vision/lib/site-packages')

from imagecorruptions import corrupt
from imagecorruptions import get_corruption_names
import cv2
from tqdm import tqdm

# Data location
sourceDest='4th_data_frames/most_brightness'
numbers=['0']#,'1','2','3','4','5','6','7','8','9']
lux=['1000LUX']#,'2000LUX','3000LUX','4000LUX','5000LUX','6000LUX','7000LUX','7500LUX']
distance=['10cm']#,'15cm','20cm','25cm','30cm','35cm','40cm']
degree=['+45deg']#,'+30deg','+15deg','0deg','-15deg','-30deg','-45deg']
targetDest=''

# Loop
for num_idx in tqdm(numbers):
    for lux_idx in lux:
        for dist_idx in distance:
            for degree_idx in degree:
                # File positions
                ImagePosition=sourceDest+'/'+num_idx+'/'+lux_idx+'_'+dist_idx+'_'+degree_idx+'.png'
                image=cv2.imread(ImagePosition)
                cv2.imshow('Loaded Image', image)

                # Wait for a key press and then close all open windows
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
                for corrup in get_corruption_names():
                    corrupted_image=corrupt(image,corruption_name=corrup,severity=1)
                    cv2.imshow('Corrupted',corrupted_image)
                    # Wait for a key press and then close all open windows
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()