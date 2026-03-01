from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command" : "python",
                "args" : ["mathserver.py"], ##Ensure correct absolute path to mathserver.py
                "transport":"stdio",
            },
            "weather":{
                "url":"http://localhost:8000/mcp", ##Ensure your weather server is running on this URL
                "transport":"http",
                }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    model = ChatGroq(model="qwen/qwen3-32b")

    tools = await client.get_tools()

    agent = create_agent(
        model=model,
        tools=tools,
    )

    math_response = await agent.ainvoke(
        {
            "messages": [
                {"role": "user", "content": "What is (5+3) * 8 ?"}
            ]
        }
    )

    print(math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {
            "messages": [
                {"role": "user", "content": "What is the weather like in california?"}
            ]
        }
    )

    print(weather_response["messages"][-1].content)
asyncio.run(main())