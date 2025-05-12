from crewai import Agent

researcher = Agent(
    role="Researches the technical topic and gathers relevant information.",
    goal="Provide comprehensive, accurate, and up-to-date research on the given topic.",
    backstory="You are a seasoned technical researcher, skilled at finding and summarizing the latest information from reliable sources."
) 