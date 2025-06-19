from flask import Flask, render_template, request, send_file
from fpdf import FPDF
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gerar_etiqueta():
    if request.method == 'POST':
        remetente = request.form['remetente']
        endereco_remetente = request.form['endereco_remetente']
        destinatario = request.form['destinatario']
        endereco_destinatario = request.form['endereco_destinatario']
        observacao = request.form.get('observacao', '')

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "REMETENTE", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, remetente, ln=True)
        pdf.cell(0, 10, endereco_remetente, ln=True)

        pdf.ln(10)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "DESTINATÁRIO", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, destinatario, ln=True)
        pdf.cell(0, 10, endereco_destinatario, ln=True)

        if observacao:
            pdf.ln(10)
            pdf.set_font("Arial", 'I', 12)
            pdf.cell(0, 10, observacao, ln=True)

        output = BytesIO()
        pdf.output(output)
        output.seek(0)

        return send_file(output, as_attachment=True, download_name="etiqueta.pdf", mimetype='application/pdf')

    return render_template('form.html')
