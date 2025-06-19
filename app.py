from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        remetente = request.form['remetente']
        destinatario = request.form['destinatario']
        produto = request.form['produto']

        pdf = FPDF()
        pdf.set_auto_page_break(auto=False)
        pdf.add_page()

        # Configurações comuns
        largura = 210  # A4 largura em mm
        altura = 297   # A4 altura em mm
        meio = altura / 2

        pdf.set_font("Arial", size=12)

        # Remetente (metade superior)
        pdf.set_xy(10, 10)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "REMETENTE", ln=True)

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, remetente)
        pdf.ln(3)
        pdf.cell(0, 10, f"Produto: {produto}", ln=True)

        # Linha divisória
        pdf.set_line_width(0.3)
        pdf.line(10, meio, largura - 10, meio)

        # Destinatário (metade inferior)
        pdf.set_xy(10, meio + 10)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "DESTINATÁRIO", ln=True)

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, destinatario)
        pdf.ln(3)
        pdf.cell(0, 10, f"Produto: {produto}", ln=True)

        # Gerar em memória
        pdf_output = io.BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)

        return send_file(pdf_output, as_attachment=True, download_name='etiqueta.pdf', mimetype='application/pdf')

    return render_template('form.html')

if __name__ == '__main__':
    app.run()
