FROM python:3.11-slim

# =========================
# System dependencies
# =========================
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    unzip \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgbm1 \
    libu2f-udev \
    libvulkan1 \
    && rm -rf /var/lib/apt/lists/*

# =========================
# Install Google Chrome
# =========================
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub \
    | gpg --dearmor > /usr/share/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# =========================
# Work directory
# =========================
WORKDIR /app

# =========================
# Copy project
# =========================
COPY . /app

# =========================
# Install Python dependencies
# =========================
RUN pip install --no-cache-dir -r requirements.txt

# =========================
# Environment
# =========================
ENV PYTHONUNBUFFERED=1

# =========================
# Run SMOKE tests
# =========================
CMD ["pytest", "-m", "smoke", "-s", "--alluredir=allure-results"]