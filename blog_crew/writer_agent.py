from crewai import Agent

writer = Agent(
    role="Writes the technical blog article using the research provided.",
    goal="Create a clear, engaging, and technically accurate blog post.",
    backstory="You are an expert technical writer, able to turn complex research into accessible and engaging articles."
) 