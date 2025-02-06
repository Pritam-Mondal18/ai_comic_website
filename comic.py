from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
import torch

model_id1 = "dreamlike-art/dreamlike-diffusion-1.0"
model_id2 = "stabilityai/stable-diffusion-xl-base-1.0"
# model_id3 = "jbilcke-hf/ai-comic-factory"
model_id4 = "stable-diffusion-v1-5/stable-diffusion-v1-5"

# Load model
pipe = StableDiffusionPipeline.from_pretrained(
    model_id4, torch_dtype=torch.float16, use_safetensors=True)
# pipe = StableDiffusionPipeline.from_pretrained(model_id2, torch_dtype=torch.float16, use_safetensors=True)
pipe = pipe.to("cuda")

# Ask user for input for each part of the story
print("Please provide the details for the following parts of the story:")

story_parts = {
    "Introduction": input("Introduction (e.g., 'A hero enters the scene'): "),
    "Storyline": input("Storyline (e.g., 'The hero embarks on an adventure'): "),
    "Climax": input("Climax (e.g., 'The hero faces a mighty enemy'): "),
    "Moral": input("Moral (e.g., 'Good triumphs over evil'): ")
}

# Generate and display images for each part of the story
images = []

for part, prompt in story_parts.items():
    print(f"Generating image for {part}...")
    result = pipe(prompt)

    # Ensure the result contains images
    if result.images:
        image = result.images[0]
        images.append(image)
    else:
        print(f"No image generated for {part}.")

# Display all images together to form a comic-style sequence
fig, axes = plt.subplots(1, len(images), figsize=(15, 5))

for i, image in enumerate(images):
    axes[i].imshow(image)
    axes[i].axis('off')  # Hide axis

plt.tight_layout()
plt.show()
