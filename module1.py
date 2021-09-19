# extract images from pdf
#!pip install fitz and PyMuPDF

import fitz

file =  'file77.pdf'

pdf = fitz.open(file)
image_list = pdf.getPageImageList(0)
for image in image_list:
    xref = image[0]
    pix =  fitz.Pixmap(pdf, xref)
    if pix.n<5:
        pix.writePNG(f'{xref}.png')
    else:
        pix1 = fitz.open(fitz.csRGB, pix)
        pix1.writePNG(f'{xref}.png')
        pix1 = None
    pix = None

print(len(image_list), 'detected')


