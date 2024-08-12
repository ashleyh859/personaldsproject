from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__,
            template_folder='../client',
            static_folder='../client/static')
@app.route('/')
def index():
    return render_template('app.html')

@app.route('/get_category_names', methods=['GET'])
def get_category_names():
    response = jsonify({
        'categories': util.get_category_names()  # Fetching categories from the utility function
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_brands', methods=['GET'])
def get_brands():
    response = jsonify({
        'brands': util.get_brands()  # Fetching brands from the utility function
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.json  # Access the JSON data sent from the frontend
    rating = float(data['rating'])  # Correct the key names based on the JSON structure
    category = data['category']
    brand = data['brand']

    estimated_price = util.predict_price(rating, category, brand)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sephora Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
