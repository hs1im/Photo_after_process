import cv2
def image_size_get_size(source,index):
    image=cv2.imread(source)
    #print(source)
    print(image.shape[index])
    return image.shape[index]