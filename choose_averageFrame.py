import cv2
import numpy as np
from tqdm import tqdm
# Datas
sourceDest='4차_데이터'
targetDest='4th_data_frames/average'
numbers=['1','0','2','3','4','5','6','7','8','9']
lux=['1000LUX','2000LUX','3000LUX','4000LUX','5000LUX','6000LUX','7000LUX','7500LUX']
distance=['10cm','15cm','20cm','25cm','30cm','35cm','40cm']
degree=['+45deg','+30deg','+15deg','0deg','-15deg','-30deg','-45deg']
videoHZ=str(30)+'Hz'
frameCount=30*3
# Loop
for num_idx in tqdm(numbers):
    for lux_idx in lux:
        for dist_idx in distance:
            for degree_idx in degree:
                # File positions
                videoPosition=sourceDest+'/'+num_idx+'/'+lux_idx+'_'+dist_idx+'_'+degree_idx+'_'+videoHZ+'.avi'
                imagePosition=targetDest+'/'+num_idx+'/'+lux_idx+'_'+dist_idx+'_'+degree_idx+'.png'
                
                # Open the .AVI file
                video_capture = cv2.VideoCapture(videoPosition)

                # Check if the video file opened successfully
                if not video_capture.isOpened():
                    print("Error: Couldn't open the video file at "+videoPosition)
                    exit()

                # init the fram
                averageFrame=None

                # Search maximum value
                #print("run at "+videoPosition)
                while True:
                    # Capture frame-by-frame
                    ret, frame = video_capture.read()

                    # If frame is not read correctly, break the loop
                    if not ret:
                        break

                    if averageFrame is None:
                        averageFrame = np.float32(frame)
                    else:
                        averageFrame += frame

                # Release the video capture object
                video_capture.release()

                # Calculate average
                if averageFrame is None:
                    print("Error in "+videoPosition)
                    continue
                averageFrame/=frameCount
                averageFrame=np.uint8(averageFrame)

                # Save the best frame
                #cv2.imshow("result",averageFrame)
                cv2.imwrite(imagePosition,averageFrame)
                #cv2.waitKey()
