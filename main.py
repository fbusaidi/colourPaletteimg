from PIL import Image
from sklearn.cluster import KMeans
from pathlib import Path
import numpy as np

# Try until a valid image path is inputed
def openImg():
    while True:
        try:
            text = input("Input image name: ").strip().strip('"')
            img = Image.open(text).convert("RGB")
            img.thumbnail((150, 150))
            return img, text
        except:
            print("Invalid image!")

def dominantCol(img):
    #images are 3d but k-means can only work with 2d so we reshape image into a 2d array using numPy libray
    pixels = np.array(img).reshape((-1, 3))

    #clustering step
    kmeans = KMeans(n_clusters=5, n_init=10, random_state=0).fit(pixels)
    centres = kmeans.cluster_centers_ #The Palette
    labels = kmeans.labels_

    #sorting the clusters
    ppc = np.bincount(labels)
    order = np.argsort(ppc)[::-1]
    palette = centres.astype(int)[order]

    return palette

def printPalette(palette):
    for r, g, b in palette:
        print(f"#{r:02x}{g:02x}{b:02x}")

def savePalette(palette, path):
    #Output palette in a .txt file with the same name as image
    outFile = Path("palette")
    outFile.mkdir(exist_ok=True) #if file doesn't exist create it
    outpath = outFile / Path(path).with_suffix(".txt").name
    with open(outpath, "w") as file:
        for r, g, b in palette:
            file.write(f"#{r:02x}{g:02x}{b:02x}\n")

    file.close()


def main():
    img, text = openImg()
    palette = dominantCol(img)
    #printPalette(palette)
    savePalette(palette, text)

main()