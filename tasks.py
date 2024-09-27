from crewai import Task
import agents

parsing_task = Task(
    description='Analyze the provided product information: {raw_product_description} and extract key features, user roles, and workflows.',
    expected_output='A structured list of user stories, features, and workflows that clearly outlines the product\'s requirements for further design processes.',
    agent=agents.requirements_parser_agent,
    output_file='parsing.txt'
)

flow_generation_task = Task(
    description='Generate descriptive details for user flow diagrams from user stories.',
    expected_output='Descriptive text for user flow diagrams describing step-by-step user interactions.',
    agent=agents.flow_generator_agent,
    output_file='flow_generation.txt'
)

# Create the corresponding mermaid_code_task
mermaid_code_task = Task(
    description='Convert user flows into Mermaid code diagrams.',
    expected_output='Mermaid code representing the user flow diagrams, illustrating step-by-step user interactions.',
    agent=agents.mermaid_code_agent,
    output_file='mermaid.txt'
)

content_formatting_task = Task(
    description='Format user stories into UI-ready content.',
    expected_output='Set of structured content elements (button texts, notifications, error messages).',
    agent=agents.content_formatter_agent,
    output_file='content_formatting.txt'
)

notification_pipeline_task = Task(
    description='Design a notification system based on user activity patterns.',
    expected_output='Proposal for a notification system with triggers, content, and timing strategies.',
    agent=agents.notification_pipeline_agent,
    output_file='notification_pipeline.txt'
)

prototyping_task = Task(
    description='Suggest wireframe components and layouts based on user flows.',
    expected_output='Verbal details of wireframe layouts representing user flow in the product interface.',
    agent=agents.prototype_helper_agent,
    output_file='prototyping.txt'
)