# -*- coding : utf-8 -*-
# coding: utf-8
import logging
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return make_response("test2")

if __name__ == '__main__':
    app.logger.setLevel(level=logging.WARNING)
    app.run(host="0.0.0.0", port=15001)
