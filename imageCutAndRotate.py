import cv2
import keyboard
import tqdm

# Fixed Values
WIDTH = 612
HEIGHT = 720

# coordinates of the box
x = 0
y = 0 # It will never move

# values of the image data
numbers=['0','1','2','3','4','5','6','7','8','9']
distance=["90cm","5cm","10cm","15cm","20cm","25cm","30cm","35cm","40cm","45cm","50cm","55cm","60cm","65cm","70cm","75cm","80cm","85cm"]
angel=["-90deg","-80deg","-70deg","-60deg","-50deg","-40deg","-30deg","-20deg","-10deg","0deg","+10deg","+20deg","+30deg","+40deg","+50deg","+60deg","+70deg","+80deg","+90deg"]
brighter=["LOW","MID","HIGH"]

# Get the image from the source
for num_idx in numbers:
    boundCheck = True
    exitSW = True
    for distance_idx in tqdm.tqdm(distance):
        for angel_idx in angel:
            for brighter_idx in brighter:
                # Get the image from the source
                sour = f'Data/Original/{num_idx}/{distance_idx}_{angel_idx}_{brighter_idx}.png'
                img = cv2.imread(sour)

                # Check the boundary of the image
                if(distance_idx=="90cm" and boundCheck):
                    boundCheck = False
                    arrowSW = True
                    while(1):
                        img_clone = img.copy()
                        cv2.rectangle(img_clone, (x, y), (x+WIDTH, y+HEIGHT), (255, 255, 0), 1)
                        cv2.imshow('Image', img_clone)
                        cv2.waitKey(1)

                        # Get the key pressed
                        if keyboard.is_pressed('a'):
                            if(arrowSW):
                                x -= 1
                                arrowSW = False
                        elif keyboard.is_pressed('d'):
                            if(arrowSW):
                                x += 1
                                arrowSW = False

                        elif keyboard.is_pressed('e'):
                            if(arrowSW):
                                x += 10
                                arrowSW = False
                        elif keyboard.is_pressed('q'):
                            if(arrowSW):
                                x -= 10
                                arrowSW = False
                        else:
                            arrowSW = True
                        
                        # Exit the loop
                        if keyboard.is_pressed('esc'):
                            if exitSW:
                                exitSW = False
                                break
                        else:
                            exitSW = True
                
                # Cut the image
                sliced = img[y:y+HEIGHT, x:x+WIDTH]

                # Rotate the image 180 degrees
                sliced = cv2.rotate(sliced, cv2.ROTATE_180)

                # Save the image
                cv2.imwrite(f'Data/Processed/{num_idx}/{distance_idx}_{angel_idx}_{brighter_idx}.png', sliced)
                #print(f'Saved: {num_idx}/{distance_idx}_{angel_idx}_{brighter_idx}.png')


# We will work seperately to 0cm distance
distance_idx = "0cm"
for angel_idx in angel:
    boundCheck = True
    for num_idx in numbers:
        for brighter_idx in brighter:
            # Get the image from the source
            sour = f'Data/Original/{num_idx}/{distance_idx}_{angel_idx}_{brighter_idx}.png'
            img = cv2.imread(sour)

            # Check the boundary of the image
            if(boundCheck):
                boundCheck = False
                arrowSW = True
                while(1):
                    img_clone = img.copy()
                    cv2.rectangle(img_clone, (x, y), (x+WIDTH, y+HEIGHT), (255, 255, 0), 1)
                    cv2.imshow('Image', img_clone)
                    cv2.waitKey(1)

                    # Get the key pressed
                    if keyboard.is_pressed('a'):
                        if(arrowSW):
                            x -= 1
                            arrowSW = False
                    elif keyboard.is_pressed('d'):
                        if(arrowSW):
                            x += 1
                            arrowSW = False

                    elif keyboard.is_pressed('e'):
                        if(arrowSW):
                            x += 10
                            arrowSW = False
                    elif keyboard.is_pressed('q'):
                        if(arrowSW):
                            x -= 10
                            arrowSW = False
                    else:
                        arrowSW = True
                    
                    # Exit the loop
                    if keyboard.is_pressed('esc'):
                        if exitSW:
                            exitSW = False
                            break
                    else:
                        exitSW = True
            
            # Cut the image
            sliced = img[y:y+HEIGHT, x:x+WIDTH]

            # Rotate the image 180 degrees
            sliced = cv2.rotate(sliced, cv2.ROTATE_180)

            # Save the image
            cv2.imwrite(f'Data/Processed/{num_idx}/{distance_idx}_{angel_idx}_{brighter_idx}.png', sliced)
            #print(f'Saved: {num_idx}/{distance_idx}_{angel_idx}_{brighter_idx}.png')




