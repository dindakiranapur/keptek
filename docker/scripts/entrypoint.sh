
#!/bin/bash
set -e

echo "================================"
echo "       KEPTEK GPU SERVER"
echo "================================"

echo "Checking NVIDIA GPU..."

nvidia-smi || true

echo "Checking Python..."

python3 --version

echo "Preparing persistent storage..."

mkdir -p /workspace

echo "Starting application..."

exec "$@"
