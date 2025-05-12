from crewai import Task
from .researcher_agent import researcher
from .writer_agent import writer
from .reviewer_agent import reviewer
from .publisher_agent import publisher
from .developer_support_agent import developer_support

def get_tasks(topic: str):
    research_task = Task(
        description=f"Research the topic: '{topic}' and provide a detailed summary with references.",
        agent=researcher,
        expected_output="A comprehensive research summary with references."
    )

    code_task = Task(
        description=f"Write supporting code examples for the blog topic: '{topic}'.",
        agent=developer_support,
        expected_output="Well-documented, functional code examples."
    )

    writing_task = Task(
        description="Write a technical blog article using the research and code provided.",
        agent=writer,
        expected_output="A draft of the technical blog article."
    )

    review_task = Task(
        description="Review the blog article for clarity, accuracy, and completeness. Suggest edits if needed.",
        agent=reviewer,
        expected_output="A reviewed and edited blog article."
    )

    publish_task = Task(
        description="Publish the final blog article and code by committing to the git repository (placeholder logic).",
        agent=publisher,
        expected_output="Blog article and code committed to git."
    )

    return [research_task, code_task, writing_task, review_task, publish_task] 