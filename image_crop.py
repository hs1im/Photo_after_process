import cv2
import numpy as np

# Load the image
img = cv2.imread('Data/Original/0/4000LUX_10cm_+15deg.png')

# Create a clone of the image to draw on
img_clone = img.copy()

cv2.namedWindow('image')

# Initial point
ix, iy = -1, -1

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
    global ix, iy, img, img_clone
    if event == cv2.EVENT_LBUTTONDOWN:
        if param[0] : 
            print(f'({ix},{iy}),({x},{y}),width={abs(ix-x)},height={abs(iy-y)}')
            cv2.imshow('aaa',slice_image(img_clone,[ix,iy],[x,y]))
            param[1]=True
            param[0]=False
        else :
            if(param[1]):
                cv2.destroyWindow('aaa')
                param[1]=False
            ix, iy = x, y
            param[0]=True
    elif event == cv2.EVENT_MOUSEMOVE:
        if ix != -1 and iy != -1:
            img_clone = img.copy()
            cv2.rectangle(img_clone, (ix, iy), (x, y), (255,255,0), 1)
            
            
        
# Set parameter to use [sw,windowOpened]
    # sw is switch of checking 'is it clicked?'
    # windowOpened is switch of checking 'is window opened?'
param=[False,False]

# Bind the function to window

cv2.setMouseCallback('image', draw_rectangle,param)

while(1):
    cv2.imshow('image', img_clone)
    if cv2.waitKey(20) & 0xFF == 27:  # press ESC to exit
        break

cv2.destroyAllWindows()