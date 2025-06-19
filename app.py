from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        remetente = request.form['remetente']
        endereco_remetente = request.form['endereco_remetente']
        destinatario = request.form['destinatario']
        endereco_destinatario = request.form['endereco_destinatario']
        transportadora = request.form['transportadora']

        buffer = gerar_pdf(remetente, endereco_remetente, destinatario, endereco_destinatario, transportadora)
        return send_file(buffer, as_attachment=True, download_name='etiqueta.pdf', mimetype='application/pdf')
    return render_template('form.html')

def gerar_pdf(remetente, endereco_remetente, destinatario, endereco_destinatario, transportadora):
    pdf = FPDF()
    pdf.add_page()

    for y in [10, 150]:
        pdf.set_xy(10, y)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "REMETENTE", ln=1)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 8, remetente, ln=1)
        pdf.cell(0, 8, endereco_remetente, ln=1)

        pdf.ln(4)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "DESTINATÁRIO", ln=1)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 8, destinatario, ln=1)
        pdf.cell(0, 8, endereco_destinatario, ln=1)

        pdf.ln(4)
        pdf.set_font("Arial", 'I', 12)
        pdf.cell(0, 8, f"{transportadora} - LIVRO", ln=1)

    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

if __name__ == '__main__':
    app.run(debug=True)
