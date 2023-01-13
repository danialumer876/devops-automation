import os
from flask import Flask

app = Flask(__name__)

@app.route('/response')
def hello():
    name = os.environ.get('NAME')
    return f'{name}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)


