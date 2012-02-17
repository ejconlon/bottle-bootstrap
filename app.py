#!/usr/bin/env python

import os
from bottle import route, run

@route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    run(host='0.0.0.0', port=port)
