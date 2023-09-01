import os

from tools.get_character_info import GetCharacterInfoTool
from tools.get_spaceship_info import GetSpaceshipInfoTool
from tools.get_spaceship_name import GetSpaceshipNameTool
from tools.get_spaceship_names import GetSpaceshipNamesTool
from tools.markdownify import MarkdownifyTool

from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.callbacks import get_openai_callback
from langchain.chat_models import AzureChatOpenAI


load_dotenv(override=True)

# Create an array with all our custom tools
tools = [
    GetCharacterInfoTool(),
    GetSpaceshipNameTool(),
    GetSpaceshipNamesTool(),
    GetSpaceshipInfoTool(),
    MarkdownifyTool()
]

# Custom callback to count tokens spent and actual price 💰
def count_tokens(chain, query):
    with get_openai_callback() as cb:
        result = chain.run(query)
        print(f'Spent a total of {cb.total_tokens} tokens')
        print(cb)
    return result

# Create the LLM configuration
llm = AzureChatOpenAI(
    openai_api_key= os.getenv("OPENAI_API_KEY"),
    openai_api_base= os.getenv("OPENAI_API_BASE"),
    openai_api_version= os.getenv("OPENAI_API_VERSION"),
    openai_api_type= os.getenv("OPENAI_API_TYPE"),
    deployment_name= os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name= os.getenv("MODEL_NAME"),
)

# Initialize the agent with tools and LLM
# Do not forget to set agent=AgentType.OPENAI_FUNCTIONS
agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

# Chat with the model
question = input("What can I do for you?\n")
prompt = """
You're an assistant for fans of the Star Wars franchise. 
Answer questions about characters and spaceships from the Star Wars universe. 
Construct markdown and style character names in bold and spaceship names in italic.
Answer questions that are not related to characters or spaceships of Star Wars with "This question, I can not answer.".

Question: {question}
"""
response = agent.run(prompt.format(question=question))
# response = count_tokens(agent, prompt.format(question=question))
# response = agent.run(prompt.format( question=question))

print(response)
