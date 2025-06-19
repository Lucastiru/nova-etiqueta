from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        remetente = request.form.get('remetente')
        destinatario = request.form.get('destinatario')
        transportadora = request.form.get('transportadora')
        conteudo = request.form.get('conteudo')

        pdf = FPDF(orientation='P', unit='mm', format=(105, 148))  # metade de uma A4
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(0, 10, "REMETENTE:", ln=True)
        pdf.multi_cell(0, 10, remetente)
        pdf.ln(5)

        pdf.cell(0, 10, "DESTINATÁRIO:", ln=True)
        pdf.multi_cell(0, 10, destinatario)
        pdf.ln(5)

        if transportadora:
            pdf.cell(0, 10, "TRANSPORTADORA:", ln=True)
            pdf.multi_cell(0, 10, transportadora)
            pdf.ln(5)

        if conteudo:
            pdf.cell(0, 10, "CONTEÚDO DA EMBALAGEM:", ln=True)
            pdf.multi_cell(0, 10, conteudo)
            pdf.ln(5)

        output = io.BytesIO()
        pdf.output(output)
        output.seek(0)
        return send_file(output, as_attachment=True, download_name="etiqueta.pdf")

    return render_template("form.html")
    
