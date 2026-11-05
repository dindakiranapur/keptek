
# KEPTEK GPU Docker Server

General-purpose Docker environment running on Modal.com.

## Features

- NVIDIA B300 GPU
- Up to 8 GPUs per container (subject to availability)
- Custom Dockerfile
- CUDA environment
- Python runtime
- FastAPI server
- Persistent Modal Volume
- GPU monitoring
- Editable application

## Requirements

- Python 3.10+
- Modal account
- Modal GPU access
- Git

## Installation

Clone repository:

    git clone https://github.com/YOUR_USERNAME/keptek.git

    cd keptek

Install dependencies:

    pip install -r requirements.txt

Login:

    modal setup

## GPU configuration

Edit config.py:

    GPU_TYPE = "B300:1"

For 8 GPUs:

    GPU_TYPE = "B300:8"

## Deploy

    modal deploy modal_app.py

## Development

    modal serve modal_app.py

## API endpoints

    /
    /health
    /gpu
    /system
    /storage

## Persistent storage

Volume name:

    keptek-storage

Container path:

    /workspace

## Stop

    modal app stop keptek

## Docker customization

Edit:

    docker/Dockerfile

Dependencies:

    docker/requirements.txt

Application:

    app/main.py

Modal configuration:

    modal_app.py
    config.py
