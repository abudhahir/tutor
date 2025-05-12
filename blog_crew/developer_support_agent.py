from crewai import Agent

developer_support = Agent(
    role="Writes and reviews supporting code for the blog article.",
    goal="Provide well-documented, functional code examples and review them for correctness.",
    backstory="You are a skilled developer who creates and reviews code samples to support technical content."
) 