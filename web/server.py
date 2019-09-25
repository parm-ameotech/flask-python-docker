from flask import Flask
from app import app

import os 

if os.environ.get("DEVELOPMENT") == "STAGING":
  app.debug = True
else:
  app.debug = False


app.run(host="0.0.0.0")