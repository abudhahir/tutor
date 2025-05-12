from crewai import Crew
from langchain_openai import OpenAI
import re
from .tasks import get_tasks
from .researcher_agent import researcher
from .writer_agent import writer
from .reviewer_agent import reviewer
from .publisher_agent import publisher
from .developer_support_agent import developer_support
import subprocess

def run_blog_workflow(topic: str):
    print(f"\n--- Starting workflow for topic: {topic} ---\n")
    tasks = get_tasks(topic)
    llm = OpenAI(
        model_name="gpt-4",
        temperature=0.7
    )
    real_crew = Crew(
        name="Technical Blog Crew",
        description="A crew that writes technical blog articles and supporting code.",
        agents=[researcher, writer, reviewer, publisher, developer_support],
        tasks=tasks,
        llm=llm,
        verbose=True
    )
    result = real_crew.kickoff()
    print(f"\n--- Workflow complete ---\n")
    print("Final Output:", result)

    front_matter = '''---
title: "Mastering AI Agentic Workflows and CrewAI: A Comprehensive Guide"
summary: A guide to understanding and building AI agentic workflows using the CrewAI framework.
date: "Mar 24 2024"
series: "Curriculum - AI"
draft: false
tags: 
    - AI 
    - CrewAI
    - Agentic Workflows
    
---
'''
    content = str(result)
    if hasattr(result, 'raw'):
        content = result.raw
    elif isinstance(result, dict) and 'content' in result:
        content = result['content']

    title = "Mastering AI Agentic Workflows and CrewAI: A Comprehensive Guide"
    filename = re.sub(r'[^a-zA-Z0-9 ]', '', title)
    filename = filename.lower().replace(' ', '-') + '.md'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(front_matter)
        f.write('\n')
        f.write(content)

    print(f"Blog post written to {filename}")

    # Commit and push to git repo
    commit_message = f"Publish blog post: {title}"
    try:
        subprocess.run(["git", "add", filename], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"Committed and pushed {filename} to git repository.")
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")

    return result 