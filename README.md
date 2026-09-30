# Colour Palette Generator
The python project generates a palette of the top 5 colours in an image and outputs them in a .txt file of the same name in the palette folder

## Getting Started
Dependencies needed:
- Python 3.6+
- [Pillow](https://pypi.org/project/pillow/)
- [scikit-learn](https://pypi.org/project/scikit-learn/)
- [NumPy](https://pypi.org/project/numpy/)

```bash
git clone https://github.com/fbusaidi/colourPaletteimg.git
cd colourPaletteimg

## Usage
```bash
python main.py

System would prompt the user to inter the image file path

*example:* Input image name: img/parrot.png

Quotes around the path are stripped automatically, so you can paste a path copied from your file explorer. If the path is invalid, you'll be asked again.

# Features
- Pixels are reshaped into a 2D array (one row per pixel, columns R, G, B).
- Uses k-means groups to form 5 clusters. Each cluster centre is one colour in the palette.
- The palette is written to `palette/<image name>.txt`

## Project structure
 
```
.
├── main.py       # the script
├── img/          # your images (optional)
└── palette/      # generated palette files
```