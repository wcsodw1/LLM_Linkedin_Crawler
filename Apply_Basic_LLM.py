
# python ice_breaker_raw.py

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain

# information = """
# Elon Reeve Musk is a business magnate and investor. He is the founder,
# CEO and chief engineer of SpaceX; angel investor,
# CEO and product architect of Tesla, Inc.;
# """

information = "Large Language model"

if __name__ == '__main__':
    print("Hello langchain")

    # summary_template = """
    #    given the information {information} about a person from I want you to create:
    #    1. a short summary
    #    2. two interesting facts about them
    # """

    summary_template = """
       given the information {information} about this technology business model:
       1. tell me about how to use LLM develop business idea
       2. two modern pragmatic application
       3. potential application
    """

    summary_prompt_template = PromptTemplate(input_variables = ["information"], template=summary_template)
    llm = ChatOpenAI(temperature = 0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    print(chain.run(information=information))