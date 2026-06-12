import os
import cloudlink

# 1. Grab the port Render assigns automatically
port_number = int(os.environ.get("PORT", 3000))

# 2. Start the server using the absolute direct module path
server = cloudlink.server.server(port=port_number, host="0.0.0.0")
server.run()
