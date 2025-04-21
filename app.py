import requests
from PIL import Image
import torch
import gradio as gr
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
    MBartForConditionalGeneration,
    MBart50TokenizerFast
)

# Force CPU usage (recommended unless you're on a CUDA-capable GPU)
device = "cpu"

# Load models
print("🔁 Loading BLIP model...")
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)

print("🔁 Loading Translation model...")
translation_tokenizer = MBart50TokenizerFast.from_pretrained("aryaumesh/english-to-telugu")
translation_model = MBartForConditionalGeneration.from_pretrained(
    "aryaumesh/english-to-telugu"
).to(device)

# Function to generate Telugu caption
def generate_telugu_caption(image: Image.Image) -> str:
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Generate English caption
    inputs = blip_processor(image, return_tensors="pt").to(device)
    output_ids = blip_model.generate(**inputs)
    english_caption = blip_processor.decode(output_ids[0], skip_special_tokens=True)

    # Translate to Telugu
    translation_inputs = translation_tokenizer(english_caption, return_tensors="pt").to(device)
    translation_output_ids = translation_model.generate(**translation_inputs)
    telugu_caption = translation_tokenizer.decode(translation_output_ids[0], skip_special_tokens=True)

    return telugu_caption

# Gradio interface
iface = gr.Interface(
    fn=generate_telugu_caption,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="📸 Telugu Caption Generator",
    description="Upload an image to generate an English caption and translate it to Telugu using BLIP and MBart."
)

# Run app
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)

