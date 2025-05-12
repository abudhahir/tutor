#!/bin/bash

# Start backend
cd backend
./run_backend.sh &
BACKEND_PID=$!
cd ..

# Start frontend
cd frontend/blog-crew-ui
npm run dev &
FRONTEND_PID=$!
cd ../..

# Print info
sleep 2
echo "\nBackend running at http://localhost:8000"
echo "Frontend running at http://localhost:5173"
echo "\nTo stop both servers, run:"
echo "  kill $BACKEND_PID $FRONTEND_PID" 