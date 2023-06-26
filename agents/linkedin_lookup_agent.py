

from tools.tools import get_profile_url
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature = 0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to theis Linkedin profile page.
                    Your answer should contain only a URL"""
    tools_for_agent1 = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]
    agent = initialize_agent(
        tools=tools_for_agent1,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_profile_url