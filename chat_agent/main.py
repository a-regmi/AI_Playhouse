from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature = 0)

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Hello Welcome to the aRegmi's Chat _ AI Assistant \n Type 'quit' to exit.")
    print("I am a specialized AI-math wizard, tell me what kind of calc you need? \n or, simply Lets chat: ")
    