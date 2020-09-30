
from datetime import date
from flask import Flask, render_template,request

from gerador import pdf
# ...
app = Flask(__name__)
app.secret_key = 'andreza'

data = date.today()

@app.route("/home")
def home():
	return render_template('cadastro.html')

@app.route("/gerar",methods=['GET', 'POST'])
def gerar():
	if request.method == 'POST':
		nome_cliente = request.form['nomeCli']
		estado_civil_cliente = request.form['EstadoCivilCli']
		profissao_cliente = request.form['profissaoCli']
		cpf_cliente = request.form['cpfCli']
		rg_cliente = request.form['rgCli']
		rua_cliente = request.form['ruaCli']
		bairro_cliente = request.form['bairroCli']
		cidade_cliente = request.form['cidadeCli']
		estado_cliente = request.form['EstadoCli']
		cep_cliente = request.form['cepCli']
		fone_cliente = request.form['telefoneCli']

		nome_procurador = request.form['nomePro']
		estado_civil_procurador = request.form['EstadoCivilPro']
		profissao_procurador = request.form['profissaoPro']
		cpf_procurador = request.form['cpfPro']
		rg_procurador = request.form['rgPro']
		rua_procurador = request.form['ruaPro']
		bairro_procurador = request.form['bairroPro']
		cidade_procurador = request.form['cidadePro']
		estado_procurador = request.form['EstadoPro']
		cep_procurador = request.form['cepPro']
		fone_procurador = request.form['telefonePro']
		motivo_procuracao = request.form['motivo']

		enviar = pdf(nome_cliente,estado_civil_cliente,profissao_cliente,cpf_cliente,rg_cliente,rua_cliente,bairro_cliente,cidade_cliente,estado_cliente,cep_cliente,fone_cliente,nome_procurador,estado_civil_procurador,profissao_procurador,cpf_procurador,rg_procurador,rua_procurador,bairro_procurador,cidade_procurador,estado_procurador,cep_procurador,fone_procurador,motivo_procuracao)
		
		return enviar
	

@app.route("/index")
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True,port=5005)