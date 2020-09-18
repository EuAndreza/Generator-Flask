from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/index")
def index():
	nome = request.args.get('nome')

	if nome:
		nome = str(nome)
	return render_template('index.html', nome = nome)

if __name__ == '__main__':
	app.run(debug=True)