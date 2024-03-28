import cv2
import numpy as np
from tqdm import tqdm

# Datas
sourceDest='4차_데이터'
targetDest_average='4th_data_frames/average'
targetDest_best='4th_data_frames/most_brightness'
dataList=['1/7500LUX_15cm_-30deg']
videoTali='_30Hz.avi'
frameCount=30*3
for data_idx in tqdm(dataList):
    # Position
    videoPosition = sourceDest+'/'+data_idx+videoTali
    averageFramePosition=targetDest_average+'/'+data_idx+'.png'
    bestFramePosition=targetDest_best+'/'+data_idx+'.png'

    # Open the .AVI file
    video_capture = cv2.VideoCapture(videoPosition)

    # Check if the video file opened successfully
    if not video_capture.isOpened():
        print("Error: Couldn't open the video file at "+videoPosition)
        exit()

    # init
    Max_Value=0
    bestFrame=None
    averageFrame=None
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # If frame is not read correctly, break the loop
        if not ret:
            break
    

            # maximum cal
        # Sum framse value
        correntVal=np.sum(frame)

        # Update biggest
        if Max_Value<correntVal : 
            Max_Value=correntVal
            bestFrame=frame

            # average cal
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
    

    # Save the frame
    cv2.imwrite(bestFramePosition,bestFrame)
    cv2.imwrite(averageFramePosition,averageFrame)