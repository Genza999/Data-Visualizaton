from flask.json import jsonify

from run import app
from utils import get_data


@app.route('/api/v1/data', methods=['GET'])
def data():
    return jsonify(get_data())


@app.route('/api/v1/categories', methods=['GET'])
def categories():
    return jsonify([
        {'country': key, 'Percentage': name}
        for key, name in get_data()['countries'].items()
    ])


@app.route('/api/v1/category/<int:category>', methods=['GET'])
def category_data(category):
    Countries = [
        country
        for country, values in get_data()['countries'].items()
        # if values[category]
    ]
    return Countries[category]
