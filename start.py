from flask import Flask
app = Flask(__name__)

@app.route('/upload')
def index():
    return 'Привет, мир!'

if __name__ == '__main__':
    app.run()