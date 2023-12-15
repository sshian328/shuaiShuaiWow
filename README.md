# shuaiShuaiWow
## Overview

This project demonstrates the use of an external API to generate images based on a given text prompt. It consists of three main files:

1. **apikey.txt**
    - Contains the API key needed to access the external API.
    - Please obtain your API key from (https://platform.stability.ai/) and replace the content of this file with your key.

2. **configSetting.py**
    - Stores configuration settings for the image generation process.
    - Modify the values of `SAMPLES`, `MODEL`, and `CLOTHES` based on your requirements.
    - SAMPLES: how many image generated each time

3. **main.py**
    - The main script that sends a request to the external API and generates images based on the provided text prompts.
    - Uses the configurations from `configSetting.py` and the API key from `apikey.txt`.
    - Ensure to install the required libraries using `pip install requests`.

## Usage

1. Fill in your API key in the `apikey.txt` file.
2. Adjust configuration settings in `configSetting.py` as needed.
3. Run the `main.py` script to generate images.

## Dependencies

- Python 3.x
- Requests library (install using `pip install requests`)

## Output

Generated images will be saved in the `./out` directory.

