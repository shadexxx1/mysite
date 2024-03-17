from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет, это мой веб-сайт!"

@app.route('/about')
def about():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()