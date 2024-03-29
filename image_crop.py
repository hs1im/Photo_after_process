import cv2

def display_image(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# replace 'your_image_path.jpg' with the path to the image you want to display



rectangles = []
current_rectangle = []
cropping = False

def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global rectangles, cropping, current_rectangle

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        current_rectangle = [(x, y)]
        cropping = True

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        current_rectangle.append((x, y))
        cropping = False # cropping is finished

        cv2.rectangle(image, current_rectangle[0], current_rectangle[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

# load the image, clone it, and setup the mouse callback function
image = cv2.imread('your_image_path.jpg')
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break

# if there are two points, then crop the region of interest
# from the image and display it
if len(current_rectangle) == 2:
    roi = clone[current_rectangle[0][1]:current_rectangle[1][1], current_rectangle[0][0]:current_rectangle[1][0]]
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)

# close all open windows
cv2.destroyAllWindows()