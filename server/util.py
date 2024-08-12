import pickle
import json
import numpy as np

__data_columns = None
__model = None

def predict_price(rating, primary_category, brand_name):
    # Ensure the category and brand names are in lowercase to match __data_columns
    primary_category = primary_category.lower()
    brand_name = brand_name.lower()

    # Get indices for the category and brand from __data_columns
    try:
        category_index = __data_columns.index(primary_category)
    except ValueError:
        category_index = -1

    try:
        brand_index = __data_columns.index(brand_name)
    except ValueError:
        brand_index = -1

    # Prepare the feature vector
    x = np.zeros(len(__data_columns))
    x[0] = rating
    if category_index >= 0:
        x[category_index] = 1
    if brand_index >= 0:
        x[brand_index] = 1

    # Predict the price using the model
    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __model

    # Update the path to the absolute path
    with open("C:/Users/ashle/OneDrive/Documents/GitHub/personaldsproject/server/artifacts/columns.json", "r") as f:
        data = json.load(f)
        __data_columns = data['data_columns']

    # Load the model from the absolute path
    if __model is None:
        with open("C:/Users/ashle/OneDrive/Documents/GitHub/personaldsproject/server/artifacts/sephora_products_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)

    print("Loading saved artifacts...done")

def get_data_columns():
    return __data_columns
def get_brands():
    # Assuming brands start from index 7 in the columns
    with open("C:/Users/ashle/OneDrive/Documents/GitHub/personaldsproject/server/artifacts/columns.json", "r") as f:
        data = json.load(f)
    return data["data_columns"][8:]  # Adjust the slice as necessary

def get_category_names():
    # Assuming the first 7 elements are the categories
    categories = ["bath & body", "fragrance", "hair", "makeup", "skincare", "tools & brushes"]
    return categories


if __name__ == '__main__':
    load_saved_artifacts()
    print("Prediction (1, 'Makeup', 'rms beauty'):", predict_price(4.56, 'Makeup', 'rms beauty'))
    print("Prediction (2, 'Skincare', 'ABBOTT'):", predict_price(2, 'Skincare', 'ABBOTT'))
