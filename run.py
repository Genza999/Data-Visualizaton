from flask import render_template, Flask
from flask_bootstrap import Bootstrap

from utils import get_data

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def main():
    data = get_data()
    return render_template('index1.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
