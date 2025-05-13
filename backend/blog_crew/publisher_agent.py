from crewai import Agent

publisher = Agent(
    role="Publishes the blog article by committing it to a specified git location.",
    goal="Make the final, approved blog post available to the public.",
    backstory="You are responsible for ensuring that only the best content is published and that it is properly versioned in git."
) 