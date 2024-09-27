from crewai import Crew, Process
import agents
import tasks

crew = Crew(
    agents=[
        agents.requirements_parser_agent,
        agents.flow_generator_agent,
        agents.content_formatter_agent,
        agents.notification_pipeline_agent,
        agents.prototype_helper_agent
    ],
    tasks=[
        tasks.parsing_task,
        tasks.flow_generation_task,
        tasks.content_formatting_task,
        tasks.notification_pipeline_task,
        tasks.prototyping_task
    ],
    manager_llm=agents.my_llm,
    process=Process.hierarchical,
    planning=True
)

result = crew.kickoff(inputs={"raw_product_description": """user experience
ai officer experience
test how well your AI performs in the real world
set behaviors for your AI
set a knowledge base for your AI
set actvity profile (waking hours, sleeping hours, working hours)
set time zone for your AI
set age
set writing style
set tons of other personality traits
Launch the AI in:
private networks (invite only)
public networks (anyone can join)
mods will be AI (have profiles, etc)
The sandbox test network (testing, tuning)
The AI officers can't create any public networks. They can only create private networks.
AI Officers can do 2 things:
Create a private network
Create an AI profile
Seed the private networks with AI profiles
Manage the private network
monitor the ai profiles activity
As a regular user, you can join either public or private networks and only chat in them, make friends. Either DMs or Community Updates. Pick a topic, and go deeper in on that topic.
We're going to need a robust, highly dynamic notifications pipeline.
Think Reddit, with a bunch of AI avatars
Then the AI officer panel allows you to deploy AI avatars into communities (edited)
The AI will engage and act on its own
Humans can join too
the AI that we allows AI officers to create will act autonomously
It will have a sleeping schedule
It will have a waking up schedule
It will have a time zone
A personality
Everything

imagine community creator
but the whol thing run by AI
it's community creator 2.0 at this point
AI officer will customize the personality of the AI
communities on the public network can only be created by staff (us)
it will be curated and heavily moderated
like for example
somebody can create an AI and then make the AI the mod of a community
But that community can only be on the private network
But AI will run itself

AI officer is like
You can have the ability to create your own AI and deploy them
This will be through a deep customization
Where the user can adjust many diff settings and create an entire new personality
Then to add into that, we do RAG so we can have a greater memory capacity
as AI tools keep evolving, we can make these bots more human like over time
eventually they will be better at interacting with humans and robots better than humans


User -> Classic Reddit Style User Experience
AI Officer ->
Network Manager (also known as Community Manager)
Community Manager

So a Network is different from a Community
A network has a collection of communities

Networks can be either
public
private

Communities can be
public
private


https://main.growthrune.com <--- Main Net
https://ucla.growthrune.com <--- Ucla Subnet

etc etc

Admin/Manager
if you creating the network/community by default you are the admin, unless it's passed to someone else or if  there are multiple admins.

on the right, we need to show case people/profiles. I'm not sure if we will have an option for "friends" right now."""})