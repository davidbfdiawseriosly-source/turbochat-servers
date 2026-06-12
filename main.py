from cloudlink import server
import os

# Render uses an environment variable for the port, default to 3000 if not found
port = int(os.environ.get("PORT", 3000))

# Initialize and run the CloudLink server
my_server = server(port=port, host="0.0.0.0")
my_server.run()
