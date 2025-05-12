# CrewAI Blog Workflow

A modular Python project for automating technical blog creation using CrewAI agents and LangChain LLMs. This project demonstrates how to orchestrate multiple specialized agents (researcher, writer, reviewer, developer, publisher) to collaboratively generate, review, and publish high-quality technical blog posts, including code samples.

## Features
- Modular agent definitions for clear separation of concerns
- Automated research, writing, code generation, review, and publishing
- Outputs blog posts in Markdown with front matter for static site generators
- Automatically commits and pushes blog posts to a GitHub repository

## Project Structure
```
blog_crew/
  researcher_agent.py
  writer_agent.py
  reviewer_agent.py
  publisher_agent.py
  developer_support_agent.py
  tasks.py
  workflow.py
crewai_blog_crew.py
README.md
requirements.txt
```

## Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/abudhahir/tutor.git
   cd tutor
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set your OpenAI API key:**
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   ```

## Usage
Run the main script to generate and publish a blog post:
```bash
python crewai_blog_crew.py
```
- The workflow will create a markdown file for the blog post.
- The file will be committed and pushed to your GitHub repository automatically.

## Customization
- Edit `blog_crew/tasks.py` to change the workflow or add new tasks.
- Update agent logic in the respective files in `blog_crew/`.
- Adjust the markdown front matter in `blog_crew/workflow.py` as needed.

## Contributing
Pull requests and suggestions are welcome! Please open an issue or submit a PR.

## License
MIT 