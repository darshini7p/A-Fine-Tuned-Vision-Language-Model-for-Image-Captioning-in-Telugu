# 🖼️ Telugu Image Caption Generator

This project uses:
- **BLIP (Bootstrapped Language-Image Pretraining)** for image captioning.
- **MBART (Multilingual BART)** for translation of English captions to Telugu.
- A simple **Gradio** interface for interaction.

## 🚀 Features

- Upload any image.
- Get a caption translated into Telugu.
- Clean UI using Gradio.
- Can be containerized and run anywhere using Docker.

## 🛠️ Technologies Used

- Python 3.10
- HuggingFace Transformers
- BLIP (`Salesforce/blip-image-captioning-base`)
- MBART (`aryaumesh/english-to-telugu`)
- Gradio
- Docker

## 🐳 Running with Docker

```bash
# Build the image
docker build -t telugu-caption-app .

# Run the container
docker run -p 7860:7860 telugu-caption-app
