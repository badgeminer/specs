from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from reportlab.graphics import renderPDF
from barcode import Code39,Code128,ISSN,PZN
from barcode.writer import SVGWriter,ImageWriter
from svglib.svglib import svg2rlg

from os import listdir
from os.path import isfile, join
onlyfiles = [join("gen\\", f) for f in listdir("gen\\") if isfile(join("gen\\", f))]


def add_image(image_path):
    my_canvas = canvas.Canvas("canvas_image.pdf")
    my_canvas.setFont('Helvetica', 12)
    x = 0
    my_canvas.drawString(180*10, 3, "SpecsScan")
    for i,p in enumerate(allI):
        if ((i%9)+(x*9)) != i:
            x += 1
            my_canvas.setStrokeColorRGB(0, 0, 0)
            my_canvas.rect((180*x)-10, 0, 1,90*9, stroke=1, fill=0)
        my_canvas.drawString(180*x, (90*(i%9))+3, p)
        drawing = svg2rlg(p)
        renderPDF.draw(drawing, my_canvas, (180*x)+50, (90*(i%9)))
        
    my_canvas.save()

allI= onlyfiles


if __name__ == '__main__':
    image_path = 'snakehead.jpg'
    add_image(image_path)

