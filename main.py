import os
from cloudlink import CloudLink

# 1. Grab the port Render gives you
port_number = int(os.environ.get("PORT", 3000))

# 2. Fire up the server cleanly using capital C and L
cl = CloudLink()
cl.host(port_number)
