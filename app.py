from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
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
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    largura = 190  # largura da folha (210 mm menos margens)
    altura_etiqueta = 135  # altura de cada etiqueta para caber duas na página

    for y in [10, 150]:  # posições verticais para 2 etiquetas
        pdf.set_xy(10, y)
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(w=largura, h=10, txt="REMETENTE", ln=1)

        pdf.set_font('Arial', '', 12)
        pdf.cell(w=largura, h=8, txt=remetente, ln=1)
        pdf.cell(w=largura, h=8, txt=endereco_remetente, ln=1)

        pdf.ln(4)
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(w=largura, h=10, txt="DESTINATÁRIO", ln=1)

        pdf.set_font('Arial', '', 12)
        pdf.cell(w=largura, h=8, txt=destinatario, ln=1)
        pdf.cell(w=largura, h=8, txt=endereco_destinatario, ln=1)

        pdf.ln(4)
        pdf.set_font('Arial', 'I', 12)
        pdf.cell(w=largura, h=8, txt=f"{transportadora} - LIVRO", ln=1)

        # borda ao redor da etiqueta
        pdf.rect(10, y, largura, altura_etiqueta)

    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

if __name__ == '__main__':
    app.run(debug=True)
