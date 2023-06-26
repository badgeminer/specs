from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from barcode import Code39,Code128,ISSN
from barcode.writer import SVGWriter,ImageWriter
with open("ISSN.png", "wb") as f:
    ISSN(str(10000000000), writer=ImageWriter()).write(f)
with open("Code128.png", "wb") as f:
    Code128(str(10000000000), writer=ImageWriter()).write(f)

def add_image(image_path):
    my_canvas = canvas.Canvas("canvas_image.pdf", pagesize=letter)
    my_canvas.setFont('Helvetica', 12)
    for i,p in enumerate(allI):
        my_canvas.drawString(0, 300*i, p)
        my_canvas.drawImage(p, 75, 300*(i))
    my_canvas.save()

allI= ["ISSN.png","Code128.png"]

if __name__ == '__main__':
    image_path = 'snakehead.jpg'
    add_image(image_path)

