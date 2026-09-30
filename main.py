from PIL import Image

def openImg():
    while True:
        try:
            text = input("Input image name: ")
            img = Image.open(text).convert("RGB").resize((150, 150))
            break
        except:
            print("Invalid image!")

            

def main():
    openImg()

main()