
# python ice_breaker.py

import requests

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == '__main__':
    print("Hello langchain")
    Link_person_LinkedinURL = True
    linkedin_profile_url = linkedin_lookup_agent(name="Bill Gates")
    Linkedin_URL = "https://www.linkedin.com/in/williamhgates/"

    summary_template = """
       given the information {information} about a person from I want you to create:
       1. a short summary
       2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables = ["information"], template=summary_template)
    llm = ChatOpenAI(temperature = 0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)


    """ 2.Scape data from Linkedin (Cost = credict) 
    Crawing Person Linkedin JSON Data, will cost "proxycurl" credict
    """

    if Link_person_LinkedinURL :
        linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    else :
        linkedin_data = scrape_linkedin_profile(linkedin_profile_url='Linkedin_URL')

    print(chain.run(information=linkedin_data))
    print('Finished')


