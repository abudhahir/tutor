# CrewAI Blog Workflow

A modular, full-stack project for automating technical blog creation using CrewAI agents and LangChain LLMs, with a modern React + Tailwind UI. The backend and frontend are now separated for clarity and deployment flexibility.

## Features
- Modular agent definitions for clear separation of concerns
- Automated research, writing, code generation, review, and publishing
- Outputs blog posts in Markdown with front matter for static site generators
- Automatically commits and pushes blog posts to a GitHub repository
- Modern React + Tailwind UI for topic input and live status

## Project Structure
```
backend/
  blog_crew/
  crewai_blog_crew.py
  main.py                # FastAPI backend
  requirements.txt
frontend/
  blog-crew-ui/          # Vite React frontend
README.md
```

## Setup (Local)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/abudhahir/tutor.git
   cd tutor
   ```

### Backend (API)
2. **Install backend dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. **Set your OpenAI API key:**
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   ```
4. **Run the backend:**
   ```bash
   uvicorn main:app --reload
   ```
   The backend will be available at http://localhost:8000

### Frontend (UI)
5. **Install frontend dependencies:**
   ```bash
   cd ../frontend/blog-crew-ui
   npm install
   ```
6. **Run the frontend:**
   ```bash
   npm run dev
   ```
   The UI will be available at [http://localhost:5173](http://localhost:5173)

## Usage
- Open the UI in your browser.
- Enter a blog topic and submit.
- Watch live status updates as the backend creates, commits, and pushes the blog post.

## Dockerized Deployment

### Backend
1. **Build the backend Docker image:**
   ```bash
   cd backend
   docker build -t crewai-blog-backend .
   ```
2. **Run the backend container:**
   ```bash
   docker run -d -p 8000:8000 -e OPENAI_API_KEY=your_openai_api_key crewai-blog-backend
   ```

### Frontend
1. **Build the frontend Docker image:**
   ```bash
   cd ../frontend/blog-crew-ui
   docker build -t crewai-blog-frontend .
   ```
2. **Run the frontend container:**
   ```bash
   docker run -d -p 5173:4173 crewai-blog-frontend
   ```
   (Vite preview runs on 4173 by default in production)

## Customization
- Edit `backend/blog_crew/tasks.py` to change the workflow or add new tasks.
- Update agent logic in the respective files in `backend/blog_crew/`.
- Adjust the markdown front matter in `backend/blog_crew/workflow.py` as needed.
- Customize the UI in `frontend/blog-crew-ui/src/`.

## Contributing
Pull requests and suggestions are welcome! Please open an issue or submit a PR.

## License
MIT 