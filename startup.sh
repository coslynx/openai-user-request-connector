#!/bin/bash

# Start the AI Connector MVP backend

set -e

echo "Starting AI Connector MVP..."

# Load environment variables
source .env

# Activate virtual environment (adjust path if needed)
source venv/bin/activate

# Start the FastAPI backend
uvicorn src.api.main:app --host 0.0.0.0 --port $PORT &

# Check if services are running (adjust checks for your specific services)
echo "Checking if services are running..."
ps aux | grep "uvicorn src.api.main:app" > /dev/null 2>&1
if [[ $? -ne 0 ]]; then
  echo "ERROR: Backend service failed to start."
  exit 1
fi

echo "AI Connector MVP started successfully."