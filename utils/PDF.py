from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_combined_pdf(titles, contents, output_pdf_path):
    def add_logos(canvas, page_number):
        left_logo_path = "Recursos/sello-blason.png"
        right_logo_path = "Recursos/DNO.png"
        canvas.drawImage(left_logo_path, 30, 725, width=50, height=50)
        canvas.drawImage(right_logo_path, letter[0] - 90, 725, width=50, height=50)
        canvas.drawCentredString(letter[0] / 2, 40, f"Página {page_number}")
        canvas.drawCentredString(letter[0] / 2, 20, "Data Network Overlock")

    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    page_number = 1  # Comenzamos desde la página 1

    for i, (title, content) in enumerate(zip(titles, contents)):
        if i != 0:  # Para evitar la superposición en la primera página
            c.showPage()
            page_number += 1  # Incrementamos el número de página para la siguiente página
        add_logos(c, page_number)
        c.setFont("Helvetica-Bold", 16)
        title_width = c.stringWidth(title, "Helvetica-Bold")
        c.drawString((letter[0] - title_width) / 2, 730, title)
        c.setFont("Courier", 9)

        lines = content.split("\n")
        y_position = 680

        for line in lines:
            if y_position <= 50:
                c.showPage()
                page_number += 1  # Incrementamos el número de página para la siguiente página
                add_logos(c, page_number)
                y_position = 750
            c.drawString(25, y_position, line)
            y_position -= 15

    c.save()

# Ejemplo de uso
titles = ["Manzana", "Cereza", "Uva"]
contents = ["Manzana\nManzana\nM\nn\nz", "Cereza\nCereza\nCereza\n\nCereza\n\n\n\nCereza\n\n\n\nCereza\n\nCereza\n\n\n\nCereza\n\nCereza\n\n\n\nCereza\n\n\nCereza\nCereza\n\n\n\nCereza\nCereza\n\n\n\nCereza\nCereza\n\n\n\nCereza\nCereza\n\n\n\nCereza\nCereza\n\n\n\nCereza\nCereza\n\n\n\nCereza\nCereza\n\n\n\nCereza\nCereza\n\n\n\nCereza\nCereza\n\n\n\nCereza\nCereza\n\n\n\nCereza\nCereza\n\n\n\nCereza\n", "U\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\nU\nV\nA\n"]
output_pdf_path = "pdf_combinado.pdf"

generate_combined_pdf(titles, contents, output_pdf_path)

print("PDF combinado creado exitosamente:", output_pdf_path)
