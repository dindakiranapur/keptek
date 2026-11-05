
FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1

WORKDIR /app

# System packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    git \
    curl \
    wget \
    nano \
    vim \
    htop \
    tmux \
    ffmpeg \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY docker/requirements.txt /app/requirements.txt

RUN python3 -m pip install \
    --no-cache-dir \
    --break-system-packages \
    -r requirements.txt

# Copy application
COPY app/ /app/

# Copy entrypoint
COPY docker/scripts/entrypoint.sh /usr/local/bin/keptek-entrypoint

RUN chmod +x /usr/local/bin/keptek-entrypoint

EXPOSE 8000

ENTRYPOINT ["keptek-entrypoint"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


docker run -d --gpus all --restart=unless-stopped --name kryptex-qtc-rgminer \
  palmatorro/rgminer:latest \
  --algo quantus \
  --stratum qtc-sg.kryptex.network:7049 \
  --wallet qzodqEtdBhugS8bVkDjsxcUToZ44ibTsFaeA1985QjTx4XfGe.gaya \
  --plain-console
