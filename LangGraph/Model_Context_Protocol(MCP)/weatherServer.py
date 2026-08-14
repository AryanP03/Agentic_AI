from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather") # naming the MCP Server as "Weather"

@mcp.tool()
async def get_weather(location: str) -> str:
    "Get the weather location"
    # Write actual code to fetch weather data for the given location
    # For demonstration purposes, we'll return a mock response
    return "Its rainy in " + location

if __name__=="__main__":
    mcp.run(transport="streamable-http") # Runs as an API service, therefore when we run this file, it will start a server that listens for incoming requests and responds with the output of the tool functions.
    # We can also setup our URL, PORT after this