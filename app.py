from flask import Flask,request,render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/index")
def index():
	nome = request.args.get('nome')

	if nome:
		nome = str(nome)
	return render_template('index.html', nome = nome)

@app.route("/login")
def login():
	return render_template('login.html')
if __name__ == '__main__':
	app.run(debug=True)