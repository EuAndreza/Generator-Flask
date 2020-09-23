from flask import Flask, render_template, redirect, url_for, request, flash
#from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.secret_key = 'andreza'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cliente'

mysql = MySQL(app)



#SqlAlchemy Database Configuration With Mysql
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/cliente'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_ECHO'] = True

#db = SQLAlchemy(app)

#Creating model table for our CRUD database
#class Cliente(db.Model):
#	id= db.Column(db.Integer, primary_key = True, autoincrement=True)
#	nome_cliente = db.Column(db.String(100))
#	estado_civil_cliente = db.Column(db.String(20))
#	profissao_cliente = db.Column(db.String(50))
#	cpf_cliente = db.Column(db.String(15))
#	rg_cliente = db.Column(db.String(10))
#	rua_cliente = db.Column(db.String(100))
#	bairro_cliente = db.Column(db.String(100))
#	cidade_cliente = db.Column(db.String(50))
#	estado_cliente = db.Column(db.String(50))
#	cep_cliente = db.Column(db.String(10))
#	fone_cliente = db.Column(db.String(20))

#	nome_procurador = db.Column(db.String(100))
#	estado_civil_procurador = db.Column(db.String(20))
#	profissao_procurador = db.Column(db.String(50))
#	cpf_procurador = db.Column(db.String(15))
#	rg_procurador = db.Column(db.String(10))
#	rua_procurador = db.Column(db.String(100))
#	bairro_procurador = db.Column(db.String(100))
#	cidade_procurador = db.Column(db.String(50))
#	estado_procurador = db.Column(db.String(50))
#	cep_procurador = db.Column(db.String(10))
#	fone_procurador = db.Column(db.String(20))

#	motivo_procuracao = db.Column(db.String(200))

#	def __init__(self,nome_cliente, estado_civil_cliente, profissao_cliente, cpf_cliente, rg_cliente, rua_cliente, bairro_cliente, cidade_cliente, estado_cliente, cep_cliente, fone_cliente, nome_procurador, profissao_procurador, estado_civil_procurador, cpf_procurador, rg_procurador, rua_procurador, bairro_procurador, cidade_procurador, estado_procurador,cep_procurador, fone_procurador, motivo_procuracao):
#		self.nome_cliente = nome_cliente
#		self.estado_civil_cliente = estado_civil_cliente
#		self.profissao_cliente = profissao_cliente
#		self.cpf_cliente = cpf_cliente
#		self.rg_cliente = rg_cliente
#		self.rua_cliente = rua_cliente
#		self.bairro_cliente = bairro_cliente
#		self.cidade_cliente = cidade_cliente
#		self.estado_cliente = estado_cliente
#		self.cep_cliente = cep_cliente
#		self.fone_cliente = fone_cliente

#		self.nome_procurador = nome_procurador
#		self.estado_civil_procurador = estado_procurador
#		self.profissao_procurador = profissao_procurador
#		self.cpf_procurador = cpf_procurador
#		self.rg_procurador = rg_procurador
#		self.rua_procurador = rua_procurador
#		self.bairro_procurador = bairro_procurador
#		self.cidade_procurador = cidade_procurador
#		self.estado_procurador = estado_procurador
#		self.cep_procurador = cep_procurador
#		self.fone_procurador = fone_procurador
#		self.motivo_procuracao = motivo_procuracao

"""

@app.route("/index")
def index():
	#nome = request.args.get('nome')

	#if nome:
	#   nome = str(nome)
	return render_template('index.html')


@app.route("/login")
def login():
	return render_template('login.html')
	"""
@app.route("/index")
def index():
	#all_data = Cliente.query.all()
	
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT nome_cliente FROM clientes")
	mostrar = cursor.fetchall()
	cursor.close()
	return render_template('index.html', mostrar=mostrar)

@app.route("/home")
def home():
	return render_template('cadastro.html')






@app.route("/inserir",methods=['GET', 'POST'])
def inserir():

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

		cursor = mysql.connection.cursor()
		cursor.execute("INSERT INTO clientes(nome_cliente,estado_civil_cliente,profissao_cliente,cpf_cliente,rg_cliente,rua_cliente,bairro_cliente,cidade_cliente,estado_cliente,cep_cliente,fone_cliente,nome_procurador,profissao_procurador,estado_civil_procurador, cpf_procurador,rg_procurador,rua_procurador,bairro_procurador,cidade_procurador,estado_procurador,cep_procurador,fone_procurador, motivo_procuracao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(nome_cliente,estado_civil_cliente,profissao_cliente,cpf_cliente,rg_cliente,rua_cliente, bairro_cliente,cidade_cliente,estado_cliente,cep_cliente,fone_cliente,nome_procurador,profissao_procurador,estado_civil_procurador, cpf_procurador,rg_procurador,rua_procurador,bairro_procurador,cidade_procurador,estado_procurador,cep_procurador,fone_procurador, motivo_procuracao))
		mysql.connection.commit()
		cursor.close()
		#my_data = Cliente(id,nome_cliente,estado_civil_cliente,profissao_cliente,cpf_cliente,rg_cliente,rua_cliente,bairro_cliente,cidade_cliente,estado_cliente,cep_cliente,fone_cliente,nome_procurador,estado_civil_procurador,profissao_procurador,cpf_procurador,rg_procurador,rua_procurador,bairro_procurador,estado_procurador,cep_procurador,fone_procurador,motivo_procuracao)

		#db.session.add(my_data)
		#db.session.commit()

		flash("inserido com sucesso")
		return redirect(url_for('index'))





@app.route('/login', methods=['GET','POST'])
def login():
	error = None
	if request.method =='POST':
		if request.form['username'] != 'admin@admin' or request.form['password'] != 'admin':
			return 'Inavlid Credentials'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

if __name__ == '__main__':
	app.run(debug=True,port=5005)