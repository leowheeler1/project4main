from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from utils.chatbot import chatbot

# Initialize Flask
app = Flask(__name__)

# Load pre-trained RandomForest model
with open("mlmodels/trained_mlmodels/rfHealthBot.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load pre-trained TF-IDF vectorizer
with open("mlmodels/trained_mlmodels/vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    user_input = data.get("text", "")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Vectorize and predict
    vector = vectorizer.transform([user_input]).toarray()
    prediction = chatbot(int(model.predict(vector)[0]))

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
