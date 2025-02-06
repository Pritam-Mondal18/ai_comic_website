from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)


@app.route("/generate-image", methods=["POST"])
def generate_image():
    try:
        # Retrieve the user input data from the frontend (image generation prompt)
        user_prompt = request.json["prompt"]

        # Send the request to Google Colab (your ML model) via an API or URL
        colab_url = "comicapikeys"  # You need to expose a Colab API URL
        response = requests.post(colab_url, json={"prompt": user_prompt})

        # Get the response from Colab and send it back to the frontend
        result = response.json()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
