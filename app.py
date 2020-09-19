from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

"""

@app.route("/index")
def index():
	#nome = request.args.get('nome')

	#if nome:
	#	nome = str(nome)
	return render_template('index.html')


@app.route("/login")
def login():
	return render_template('login.html')
	"""
@app.route("/home")
def home():
	return render_template('home.html')

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
	app.run(debug=True)