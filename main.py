from PIL import Image
import numpy as np

# Try until a valid image path is inputed
def openImg():
    while True:
        try:
            text = input("Input image name: ")
            img = Image.open(text).convert("RGB")
            img.thumbnail((150, 150))
            return img
        except:
            print("Invalid image!")

def dominantCol(img):
    #images are 3d but k-means can only work with 2d so we reshape image into a 2d array using numPy libray
    array = np.array(img).reshape((-1, 3))





def main():
    img = openImg()
    dominantCol(img)

main()