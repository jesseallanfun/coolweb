# Menggunakan image dasar Ubuntu (Linux)
FROM ubuntu:22.04

# Set working directory
WORKDIR /app

# Install Python dan dependencies untuk menjalankan file batch
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    dos2unix \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Salin semua file dari host ke container
COPY . .

# Konversi file batch (.bat) ke format Unix agar bisa dijalankan
RUN dos2unix *.bat

# Install dependencies Python (jika ada)
RUN pip3 install -r requirements.txt || true

# Jalankan file batch
CMD ["bash", "-c", "chmod +x show.bat && ./show.bat"]
