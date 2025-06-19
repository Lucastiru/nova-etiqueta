from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        remetente = request.form.get('remetente')
        destinatario = request.form.get('destinatario')
        transportadora = request.form.get('transportadora')
        tipo_mercadoria = request.form.get('tipo_mercadoria')

        pdf = FPDF()
        pdf.add_page()

        for i in range(2):  # Duas etiquetas por folha
            if i > 0:
                pdf.set_y(150)
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, f"Remetente: {remetente}", ln=True)
            pdf.cell(0, 10, f"Destinatário: {destinatario}", ln=True)
            pdf.cell(0, 10, f"Transportadora: {transportadora}", ln=True)
            pdf.cell(0, 10, f"Tipo da mercadoria: {tipo_mercadoria}", ln=True)
            pdf.ln(10)

        buffer = io.BytesIO()
        pdf.output(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name="etiquetas.pdf", mimetype='application/pdf')

    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
