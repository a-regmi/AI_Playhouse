from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    api_key = os.getenv('OPENAI_API_KEY')
    print("API Key loaded:", bool(api_key))
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in env variables")
    
    try: 
        model = ChatOpenAI(temperature = 0)

        tools = []
        agent_executor = create_react_agent(model, tools)

        print("Hello Welcome to the aRegmi's Chat Agent \nType 'quit' to exit.")
        print("I am a chat agent, tell me what are you curious about today ? \nor, simply Lets chat: ")
        
        while True:
            user_input = input("\nYou: ").strip()

            if user_input == "quit":
                break

            print("\nAssistant: ", end="") #No new default line 
            for chunk in agent_executor.stream(
                {"messages" : [HumanMessage(content = user_input)]}
            ):
                if "agent" in chunk and "messages" in chunk["agent"]:
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end = "")
            print()

    except Exception as e:
        print(f"Error initializing ChatOpenAI: {str(e)}")
        return

if __name__ == "__main__":
    main()
