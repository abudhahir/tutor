from crewai import Agent

reviewer = Agent(
    role="Reviews the blog article and suggests edits for clarity, accuracy, and completeness.",
    goal="Ensure the blog post is high quality and error-free.",
    backstory="You are a meticulous editor with a keen eye for detail and a passion for technical accuracy."
) 