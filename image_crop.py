import cv2
import numpy as np
def process_image():
    # Load the image
    img = cv2.imread('Data/Original/0/4000LUX_10cm_+15deg.png')
    # Create a clone of the image to draw on
    img_clone = img.copy()

    cv2.namedWindow('image')

    # Initial point
    ix, iy = -1, -1

    # Initial switch
    sw=False
    windowOpened=False

    # Save cutted image
    imageSliced=None

    # Image cutting  function
    def slice_image(img, start, end):
        # Check x and y to not twist it's coordinate
        for i in range(2):
            if(start[i]>end[i]):
                ms=start[i]
                start[i]=end[i]
                end[i]=ms

        # Return sliced image
        return img[start[1]:end[1], start[0]:end[0]]

    # Mouse callback function
    def draw_rectangle(event, x, y, flags, param):
        nonlocal ix, iy, img, img_clone,sw,windowOpened,imageSliced
        if event == cv2.EVENT_LBUTTONDOWN:
            if sw : 
                print(f'({ix},{iy}),({x},{y}),width={abs(ix-x)},height={abs(iy-y)}')
                imageSliced=slice_image(img_clone,[ix+1,iy+1],[x,y])
                cv2.imshow('example',imageSliced)
                windowOpened=True
                sw=False
            else :
                if(windowOpened):
                    cv2.destroyWindow('example')
                    windowOpened=False
                ix, iy = x, y
                sw=True
        elif event == cv2.EVENT_MOUSEMOVE:
            if ix != -1 and iy != -1:
                img_clone = img.copy()
                cv2.rectangle(img_clone, (ix, iy), (x, y), (255,255,0), 1)


    # Set parameter to use [sw, windowOpened, sliced image]
        # sw is switch of checking 'is it clicked?'
        # windowOpened is switch of checking 'is window opened?'
        # sliced image is image came from 
    param=[False,False,None]

    # Bind the function to window

    cv2.setMouseCallback('image', draw_rectangle,param)

    while(1):
        cv2.imshow('image', img_clone)
        if cv2.waitKey(1) & 0xFF == 32:  # Press SPACE to save file
            if windowOpened: # When the image is showing
                print('Saved')
                cv2.imwrite('Data/Processed/test.png',imageSliced)
        if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
            break

    cv2.destroyAllWindows()
process_image()