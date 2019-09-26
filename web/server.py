from multiprocessing import Process
import threading

from flask import Flask
from app import app

import os 

if os.environ.get("DEVELOPMENT") == "STAGING":
  app.debug = True
else:
  app.debug = False


def daemon_process():
    print("daemon is working")
    threading.Timer(1, daemon_process).start()

def flask_process():
    app.run(host="0.0.0.0")


if __name__ == '__main__':
  p1 = Process(target=daemon_process)
  p1.start()
  p2 = Process(target=flask_process)
  p2.start()

  p1.join()
  p2.join()