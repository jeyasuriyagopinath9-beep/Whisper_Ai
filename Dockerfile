# Use Python 3.11 slim base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install ffmpeg for audio processing
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Copy the rest of the app
COPY . .

# Expose port 9000 for API
EXPOSE 9000

# Run the app
CMD ["python", "app.py"]
