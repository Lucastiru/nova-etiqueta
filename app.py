from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    remetente_nome = request.form['remetente_nome']
    remetente_endereco = request.form['remetente_endereco']
    destinatario_nome = request.form['destinatario_nome']
    destinatario_endereco = request.form['destinatario_endereco']

    pdf = FPDF('P', 'mm', (150, 100))
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "REMETENTE", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"{remetente_nome}\n{remetente_endereco}")
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "DESTINATÁRIO", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"{destinatario_nome}\n{destinatario_endereco}")

    output = io.BytesIO()
    pdf.output(output)
    output.seek(0)
    return send_file(output, as_attachment=True, download_name="etiqueta.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', p
