import numpy as np
from flask_app.app import flask_app

def main(a, b):
    print(a)
    print(b)
    fa = flask_app("doggo-dev-chart", settings="settings.json")
    fa.app.run(host="0.0.0.0")


if __name__ == "__main__":
    main()
