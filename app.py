import numpy as np
from flask import Flask, request,render_template, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods = ['GET','POST'])
def home():
    data = 'hello world'
    return jsonify({'data':data})

@app.route('/predict/')
def predict():

    years = request.args.get('years')
    float_features = [float(years)]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    input_feature = float_features[0]
    output = round(prediction[0], 2)

    return jsonify({'Salary': str(output)})

if __name__ == "__main__":
    app.run(debug=True)
