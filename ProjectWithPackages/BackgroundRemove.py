from PIL import Image
from rembg import remove

imgfile = Image.open("photo-1.jpeg")
outfile = remove(imgfile)
outfile.save("imag-1.png")

