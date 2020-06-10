
import itertools
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)

def export_to_pdf(data):
    c = canvas.Canvas("grilla-alumnos.pdf", pagesize=A4)
    w, h = A4
    max_rows_per_page = 45
    # Margin.
    x_offset = 50
    y_offset = 50
    # Space between rows.
    padding = 15
                
    xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
                
    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()
    c.save()