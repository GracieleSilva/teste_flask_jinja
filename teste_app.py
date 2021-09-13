from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_all():
	return render_template('index.html', students = [{"nome":"Graciele"},{"nome":"davi"},{"nome":"daniel"}] )

app.run(debug = True)