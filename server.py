from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok
from diffusers import StableDiffusionPipeline
import torch

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)

# Load your model (stable-diffusion, or any model you're using)
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True)
pipe = pipe.to("cuda")


@app.route("/generate_comic", methods=["POST"])
def generate_comic():
    # Extract the story parts from the request
    data = request.get_json()
    introduction = data.get("introduction")
    storyline = data.get("storyline")
    climax = data.get("climax")
    moral = data.get("moral")

    # Create a prompt for each part of the story
    prompts = {
        "Introduction": introduction,
        "Storyline": storyline,
        "Climax": climax,
        "Moral": moral
    }

    # Generate images for each story part
    images = []
    for part, prompt in prompts.items():
        print(f"Generating image for {part}...")  # For debugging
        result = pipe(prompt)
        if result.images:
            image = result.images[0]
            # Save the image temporarily
            image_path = f"/content/{part}.png"
            image.save(image_path)
            images.append(f"http://{ngrok_url}/{part}.png")
        else:
            images.append(None)

    return jsonify({"images": images})


# Expose the app to the public via ngrok
ngrok_url = ngrok.connect(5000).public_url
print(f"API running on {ngrok_url}")

app.run(port=5000)
