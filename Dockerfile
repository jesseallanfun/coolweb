# Menggunakan image dasar Windows
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Set working directory
WORKDIR C:\\app

# Copy semua file dari repository ke dalam Docker container
COPY . .

# Install Python di Windows
RUN powershell -Command \
    $ErrorActionPreference = 'Stop'; \
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe" -OutFile "python-installer.exe"; \
    Start-Process python-installer.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -NoNewWindow -Wait

# Jalankan Downloads.bat
RUN cmd /c Downloads.bat

# Set default command untuk menjalankan script show.bat
CMD ["cmd", "/c", "show.bat"]
