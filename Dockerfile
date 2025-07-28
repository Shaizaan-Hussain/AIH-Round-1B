FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Install OS dependencies for PyMuPDF
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libgl1-mesa-glx \
 && rm -rf /var/lib/apt/lists/*

# Copy dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code into container
COPY . .

# Set default command
ENTRYPOINT ["python", "round1b_persona_pdf_analyzer.py"]
