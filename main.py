from flask_app.app import flask_app

if __name__ == "__main__":
    fa = flask_app("doggo-dev-chart", settings="settings.json")
    fa.app.run(host="0.0.0.0", port=80)
    pass
