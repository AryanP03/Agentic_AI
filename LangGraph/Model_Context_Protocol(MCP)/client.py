# We are creating MCP client, which should be able to interact with all the server(weatherServer and mathServer here)
from http import client

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

import asyncio # asyncio is a library to write concurrent code using the async/await syntax. It provides a framework for writing asynchronous programs in Python. It allows you to run multiple tasks concurrently, making it useful for I/O-bound and high-level structured network code.

async def main():
    client=MultiServerMCPClient(
        {
              "math":{
                  "command": "python",
                  "args": [
                       "D:/Agentic_AI/LangGraph/Model_Context_Protocol(MCP)/mathserver.py"
                      ], ## Ensure correct absolute path to the mathserver.py file
                  "transport": "stdio"
              },
              "weather":{
                  "url": "http://127.0.0.1:8000/mcp", ## Ensure server is running here
                  "transport": "streamable-http"
              }

        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")  # Set the GROQ API key from environment variables

    tools=await client.get_tools() # Get the tools from the MCP servers
    model=ChatGroq(model="llama-3.3-70b-versatile") # Initialize the ChatGroq model
    agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
You are a helpful assistant.

When solving a problem that requires multiple tools:
1. Call the first tool.
2. Wait for its result.
3. Use that result as an argument to the next tool.
4. Never place one tool call inside the arguments of another tool call.
"""
) # Create a ReAct agent with the model and tools

    math_response = await agent.ainvoke(
    {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
)

    print("Math response:", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
    {"messages": [{"role": "user", "content": "what is the weather in California?"}]}
)
    print("Weather response:", weather_response['messages'][-1].content)
    for message in weather_response["messages"]:
        print(type(message).__name__, ":", message.content)

asyncio.run(main())

## Please have a look at the "Our_mcp_architecture.png" file in this folder itself, which explain you the entire working of our app



