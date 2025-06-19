from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/gerar_etiqueta', methods=['POST'])
def gerar_etiqueta():
    remetente = request.form['remetente']
    endereco_remetente = request.form['endereco_remetente']
    destinatario = request.form['destinatario']
    endereco_destinatario = request.form['endereco_destinatario']
    observacao = request.form['observacao']

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()

    for i in range(2):  #
