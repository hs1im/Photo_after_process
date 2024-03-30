import cv2
def image_size_get_height(source):
    image=cv2.imread(source)
    print(source)
    print(image.shape[0])
    return image.shape[0]