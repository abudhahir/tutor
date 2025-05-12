#!/bin/bash
# Run FastAPI backend locally with hot reload
echo "Starting FastAPI backend on http://127.0.0.1:8000"
uvicorn main:app --reload 