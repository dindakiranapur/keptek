
#!/bin/bash
set -e

echo "Deploying KEPTEK..."

modal deploy modal_app.py

echo "Deployment completed."
