import asyncio
import os
from cloudlink import cloudlink

async def main():
    # 1. Read Render's assigned port dynamically (defaults to 3000)
    port_number = int(os.environ.get("PORT", 3000))
    
    # 2. Instantiate the parent cloudlink object properly
    cl = cloudlink() 
    
    # 3. Initialize the server object (Leave this blank or use logs=True)
    my_server = cl.server(logs=True) 
    
    # 4. Pass the network host and port settings inside the RUN block!
    await my_server.run(ip="0.0.0.0", port=port_number)

if __name__ == "__main__":
    asyncio.run(main())
