import asyncio
import os
from cloudlink import server

async def main():
    # Read Render's assigned port dynamically
    port = int(os.environ.get("PORT", 3000))
    
    # Initialize the server
    my_server = server(port=port, host="0.0.0.0")
    
    # Run the server using its asynchronous framework
    await my_server.run()

if __name__ == "__main__":
    asyncio.run(main())
