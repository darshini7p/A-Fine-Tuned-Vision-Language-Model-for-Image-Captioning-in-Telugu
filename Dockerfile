# Dockerfile
FROM python:3.10-slim

# System-level dependencies
RUN apt-get update && apt-get install -y git ffmpeg libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /app

# Copy files
COPY app.py app.py
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Gradio's default port
EXPOSE 7860

# Run the app
CMD ["python", "app.py"]
