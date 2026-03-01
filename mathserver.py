from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int , b:int) -> int:
    """ Add Two Numbers"""
    return a+b

@mcp.tool()
def multiply(a:int , b:int) -> int:
    """ Multiply Two Number"""
    return a*b

# This Transport = "stdio" argument tells the server to:

# Use standard input/output (stdin and stdout) to receive and respond to tool function calls

if __name__ =="__main__":
    mcp.run(transport ="stdio")