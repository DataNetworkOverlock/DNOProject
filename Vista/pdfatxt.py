from fpdf import FPDF

def text_to_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Abre el archivo de texto de entrada y lee su contenido
    with open(input_file, "r") as file:
        content = file.read()

    # Agrega el contenido del archivo de texto al archivo PDF
    pdf.multi_cell(190, 10, txt=content, border=0, align="L")

    # Guarda el archivo PDF
    pdf.output(output_file)

if __name__ == "__main__":
    input_file = "D:/trabajos/Tesis/Repositorio/DNOProject/RecursosTXTsCereza.txt"  # Nombre del archivo de texto de entrada
    output_file = "output.pdf"  # Nombre del archivo PDF de salida

    text_to_pdf(input_file, output_file)
    print(f"Se ha creado el archivo PDF: {output_file}")
