import asyncio
import time
import os
import datetime
#from perception import extract_perception
#from memory import MemoryManager, MemoryItem
#from decision import generate_plan
#from action import execute_tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
 # use this to connect to running server

import shutil
import sys

def log(stage: str, msg: str):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] [{stage}] {msg}")

max_steps = 3
async def generate_with_timeout(client, system_prompt, timeout=10):
    """Generate content with a timeout"""
    print("Starting LLM generation...")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=system_prompt
    )

    print("LLM generation completed")
    return response   
    
async def main():

    
    # Create a single MCP Multiply server connection
    print("Establishing connection to RAG server...")
    server_params = StdioServerParameters(
        command="python",
        args=["mcpRAG.py"]
    )
    
    
    
    
    
    
    async with stdio_client(server_params) as (read, write):
        
        print("Connection established, creating session...")
        async with ClientSession(read, write) as session:
            
    
             print("Session created, initializing...")
             await session.initialize()
             

             # Get available tools
             print("Requesting tool list...")
             tools = await session.list_tools()
             
        
             print("Tools available:")
            #print(tools.model_dump())
  
                    
             tools_description = []
             tools_list = []
             for i in range(0,len(tools.tools)):
                tools_list.append(tools.tools[i].name)

        
             print(f"Tools list: {tools_list}")    
             for i in range(0,len(tools.tools)):
                print(f"Tool_{i+1}: {tools.tools[i].name} - {tools.tools[i].description}")
                tools_description.append(f"{tools.tools[i].name}: {tools.tools[i].inputSchema.values()}")

                
             print(f"Tools description:{tools_description}")

                # Create a system prompt
                

if __name__ == "__main__":
    asyncio.run(main())