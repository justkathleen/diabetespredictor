from flask import Flask, render_template, request
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    patientName = request.form['name']

    model = pickle.load(open('/Users/angelinakathleen/Downloads/model96.joblib', 'rb'))
    return patientName


if __name__ == '__main__':
    app.run(port=3000, debug = True)
