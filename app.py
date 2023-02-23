from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/data', methods = ['GET'])
def get_data():

    data = pd.DataFrame({
            "Name": 'abc',
            "Molecular Formula": "H20",
            "Molecular Weight": [20],
            "Smile" :"HHO",
            "Density": [10],
            "Hazard": "xyz",
            "Category": "Red"
        })
    
    response = jsonify(data.to_dict())

    response.headers.add('Content-Type', 'application/json')

    return response


if __name__ == "__main__python ":
    app.run(debug = True)