import base64
import requests
import os
import configSetting as cfg
from PIL import Image
import time

url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

prompt = f"a {cfg.MODEL}, long blonde hair, wearing ({cfg.CLOTHES}), detailed skin, intricate detailed, trending on artstation, coffee shop, city,"
body = {
  "steps": 40,
  "width": 1024,
  "height": 1024,
  "seed": 0,
  "cfg_scale": 5,
  "samples": cfg.SAMPLES,
  "style_preset": "photographic",
  "text_prompts": [
    {
      "text": prompt,
      "weight": 1
    },
    {
      "text": "blurry, bad, Cross-eyed",
      "weight": -1
    }
  ],
}

api_key = ''
with open('apikey.txt', 'r') as file:
    # Read the content of the file into a variable
    api_key = file.read().strip()

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": api_key,
}
print(f"sending request, prompt={prompt}")
response = requests.post(
  url,
  headers=headers,
  json=body,
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

# Print response headers for debugging
print("Response Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# You can also print the status code and response content
print("\nStatus Code:", response.status_code)

data = response.json()

# make sure the out directory exists
if not os.path.exists("./out"):
    os.makedirs("./out")

for i, image in enumerate(data["artifacts"]):
    image_data = base64.b64decode(image["base64"])
    
    # Get the current timestamp as a string
    current_time = time.strftime("%Y%m%d%H%M%S")
    
    # Save the image with timestamp in the filename
    img_path = f'./out/txt2img_{image["seed"]}_{current_time}.png'
    with open(img_path, "wb") as f:
        f.write(image_data)
    
    # Open the image using PIL
    img = Image.open(img_path)
    
    # Display the image (opens the default image viewer)
    img.show()    