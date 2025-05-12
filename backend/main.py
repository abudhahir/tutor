from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import queue
import threading
import datetime
from blog_crew.workflow import run_blog_workflow
from dotenv import load_dotenv
import openai
import os
from openai import OpenAI

load_dotenv()

app = FastAPI()

# Allow local dev frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

status_queues = {}

@app.post("/api/create-blog")
async def create_blog(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()
    topic = data.get("topic")
    if not topic:
        return JSONResponse({"error": "No topic provided"}, status_code=400)

    q = queue.Queue()
    status_queues["current"] = q

    def run_workflow():
        def status_callback(msg):
            q.put(msg)
        run_blog_workflow(topic, status_callback=status_callback)
        q.put("DONE")

    background_tasks.add_task(run_workflow)
    return {"status": "started"}

@app.get("/api/blog-status")
def blog_status():
    def event_stream():
        q = status_queues.get("current")
        if not q:
            yield "data: No status yet\n\n"
            return
        while True:
            msg = q.get()
            yield f"data: {msg}\n\n"
            if msg == "DONE":
                break
    return StreamingResponse(event_stream(), media_type="text/event-stream")

client = OpenAI()  # This will auto-pick from env if set 