from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from reportlab.graphics import renderPDF
from barcode import Code39,Code128,ISSN,PZN
from barcode.writer import SVGWriter,ImageWriter
from svglib.svglib import svg2rlg

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("gen\\") if isfile(join("gen\\", f))]


def add_image(image_path):
    my_canvas = canvas.Canvas("canvas_image.pdf")
    my_canvas.setFont('Helvetica', 12)
    x = 0
    my_canvas.drawString(5, 3, "SpecsScan")
    for i,P in enumerate(allI):
        p = str(P).removesuffix(".svg")
        if ((i%8)+(x*8)) != i:
            x += 1
            my_canvas.setStrokeColorRGB(0, 0, 0)
            my_canvas.rect((190*x)-10, 0, 1,90*9, stroke=1, fill=0)
        my_canvas.drawString((190*x)+5, (90*((i%8)+1))+10, p)
        drawing = svg2rlg("gen\\"+P)
        renderPDF.draw(drawing, my_canvas, (190*x)+60, (90*((i%8)+1)))
        
    my_canvas.save()

allI= onlyfiles


if __name__ == '__main__':
    image_path = 'snakehead.jpg'
    add_image(image_path)

