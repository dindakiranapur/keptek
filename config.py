
import os

APP_NAME = "keptek"

# GPU configuration
GPU_TYPE = os.getenv("GPU_TYPE", "B300:1")

# Compute resources
CPU = int(os.getenv("CPU", "16"))
MEMORY = int(os.getenv("MEMORY", "65536"))
EPHEMERAL_DISK = int(
    os.getenv("EPHEMERAL_DISK", "100000")
)

# Persistent storage
VOLUME_NAME = "keptek-storage"
VOLUME_PATH = "/workspace"

# Server
PORT = 8000

# Keep server warm after requests
SCALEDOWN_WINDOW = 3600
