import numpy as np
from flask_app.app import flask_app

def main():
    fa = flask_app("doggo-dev-chart", settings="settings.json")
    fa.app.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    main()
