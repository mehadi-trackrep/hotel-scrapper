# Dockerfile
FROM python:3.11-slim

# 1. Set environment and install system dependencies
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    wget \
    git \
    libglib2.0-0 \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libx11-xcb1 \
    libxext6 \
    libxss1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libharfbuzz0b \
    libgtk-3-0 \
    libgbm1 \
    && apt-get clean

WORKDIR /app

# 2. Install pip dependencies
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv pip install --system --no-deps .

# 3. Install Playwright & Uvicorn correctly
RUN uv pip install --system playwright && playwright install chromium
RUN uv pip install --system uvicorn

# Copy FastAPI app code into container (adjust if needed)
COPY ./app ./app
COPY ./scraper ./scraper

# 5. Default command (optional for FastAPI)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
