from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio") # Use standard input/output (stdin/stdout) to receive and respond to tool function calls
    # Therefore when we run this file, we dont get to see a server running, instead we can call the tool functions directly from the command line or from another program that communicates with this server using standard input/output.