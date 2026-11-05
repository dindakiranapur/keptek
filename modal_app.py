
import modal

from config import (
    APP_NAME,
    GPU_TYPE,
    CPU,
    MEMORY,
    EPHEMERAL_DISK,
    VOLUME_NAME,
    VOLUME_PATH,
    SCALEDOWN_WINDOW,
)

app = modal.App(APP_NAME)

volume = modal.Volume.from_name(
    VOLUME_NAME,
    create_if_missing=True,
)

image = modal.Image.from_dockerfile(
    "docker/Dockerfile",
    context_dir=".",
)

@app.function(
    image=image,
    gpu=GPU_TYPE,
    cpu=CPU,
    memory=MEMORY,
    ephemeral_disk=EPHEMERAL_DISK,
    volumes={VOLUME_PATH: volume},
    timeout=86400,
    min_containers=1,
    max_containers=1,
    scaledown_window=SCALEDOWN_WINDOW,
)
@modal.concurrent(max_inputs=100)
@modal.asgi_app(requires_proxy_auth=True)
def web():
    from main import app as fastapi_app
    return fastapi_app
