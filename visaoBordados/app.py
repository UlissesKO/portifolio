from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contact.html')

@app.route('/produtos')
def produtos():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)