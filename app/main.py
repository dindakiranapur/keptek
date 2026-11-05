
import os
import subprocess
from pathlib import Path

import psutil
from fastapi import FastAPI

app = FastAPI(
    title="KEPTEK GPU SERVER",
    version="1.0.0",
)

STORAGE = Path("/workspace")


@app.get("/")
def home():
    return {
        "name": "KEPTEK",
        "status": "running",
        "storage": str(STORAGE),
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
    }


@app.get("/gpu")
def gpu():
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            capture_output=True,
            text=True,
            timeout=20,
        )

        return {
            "output": result.stdout,
            "error": result.stderr,
        }

    except Exception as error:
        return {"error": str(error)}


@app.get("/system")
def system():
    return {
        "python": os.sys.version,
        "cpu_count": os.cpu_count(),
        "memory_gb": round(
            psutil.virtual_memory().total / 1024**3,
            2,
        ),
    }


@app.get("/storage")
def storage():
    STORAGE.mkdir(parents=True, exist_ok=True)

    return {
        "path": str(STORAGE),
        "files": [
            str(p.relative_to(STORAGE))
            for p in STORAGE.rglob("*")
            if p.is_file()
        ],
    }


@app.post("/storage/write")
def storage_write():
    STORAGE.mkdir(parents=True, exist_ok=True)

    file = STORAGE / "keptek-test.txt"
    file.write_text(
        "KEPTEK persistent storage is working.",
        encoding="utf-8",
    )

    return {
        "status": "written",
        "file": str(file),
    }
